import csv
from pathlib import Path

CSV_DIR = Path(__file__).parent / "data"

# 判定
# 異常
NO_POWER_HOURS_ALERT = 24       # 電気ゼロが24時間連続
NIGHT_GAS_HOURS_ALERT = 3       # 深夜ガスが3時間連続
 
# やや注意
NO_POWER_HOURS_WARN = 12        # 電気ゼロが12時間連続
NIGHT_GAS_HOURS_WARN = 2        # 深夜ガスが2時間連続
GAS_LOW_RATIO = 0.5             # ガス総使用量が平常時の50%未満

NIGHT_HOURS = [23, 0, 1, 2, 3, 4]
BASELINE_FILE = "normal_data.csv"

META = {
    "通常": {
        "file": "normal_data.csv",
        "note": None,
    },
    "やや注意": {
        "file": "caution_data.csv",
        "note": "ガスの利用がいつもより少なめです",
    },
    "異常": {
        "file": "abnormal_data.csv",
        "note": None,
    },
    "熱中症リスク(夏場)": {
        "file": "abnormal_data.csv",
        "status": "異常", 
        "last_electricity": "前日 19:32",
        "last_gas": "23:00",
        "note": None,
    },
}


def _read(filename):
    """CSVを読んで、時刻・電気・ガスの3つのリストを返す"""
    hours, electricity, gas = [], [], []
    with open(CSV_DIR / filename, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            hours.append(row["Time"])
            electricity.append(float(row["Electricity_kWh"]))
            gas.append(float(row["Gas_m3"]))
    return hours, electricity, gas


def _max_streak(values, used):
    best = current = 0
    for v in values:
        current = current + 1 if used(v) else 0
        best = max(best, current)
    return best

def _night_gas(hours, gas):
    """深夜帯のガス使用量を、時刻順（23時→4時）に並べて返す"""
    by_hour = {int(t.split(":")[0]): g for t, g in zip(hours, gas)}
    return [by_hour.get(h, 0) for h in NIGHT_HOURS]

def _baseline_gas_total():
    """平常時の1日あたりガス総使用量"""
    _, _, gas = _read(BASELINE_FILE)
    return sum(gas)

def _last_used(hours, values):
    """最後に使用量が0より大きかった時刻と値を返す。一度も使っていなければ None"""
    for t, v in zip(reversed(hours), reversed(values)):
        if v > 0:
            return {"time": t, "value": v}
    return None

def _judge(hours, electricity, gas):
    """通常 / やや注意 / 異常 を判定する。異常を先に見る"""
    no_power = _max_streak(electricity, lambda v: v == 0)
    night = _max_streak(_night_gas(hours, gas), lambda v: v > 0)
 
    # --- 異常 ---
    if no_power >= NO_POWER_HOURS_ALERT:
        return "異常"
    if night >= NIGHT_GAS_HOURS_ALERT:
        return "異常"
 
    # --- やや注意 ---
    if no_power >= NO_POWER_HOURS_WARN:
        return "やや注意"
    if night >= NIGHT_GAS_HOURS_WARN:
        return "やや注意"
 
    baseline = _baseline_gas_total()
    if baseline > 0 and sum(gas) < baseline * GAS_LOW_RATIO:
        return "やや注意"
 
    return "通常"


def get(scenario):
    meta = META[scenario]
    hours, electricity, gas = _read(meta["file"])

    return {
        "updated_at": "2026/09/10 09:32",
        "hours": hours,
        "electricity": electricity,
        "gas": gas,
        "last_electricity": _last_used(hours, electricity),
        "last_gas": _last_used(hours, gas),
        "note": meta["note"],
        "status": _judge(hours, electricity, gas), 
    }


if __name__ == "__main__":
    base = _baseline_gas_total()
    print(f"ベースライン(ガス総使用量): {base:.1f} m3  / 注意の境界: {base * GAS_LOW_RATIO:.2f} m3\n")
    for name in META:
        d = get(name)
        print(
            f"{name:5s} -> {d['status']:5s} "
            f"ガス計 {sum(d['gas']):.1f} m3  "
            f"電気計 {sum(d['electricity']):.1f} kWh  "
            f"件数 {len(d['electricity'])}"
            f"最終利用 電気: {d['last_electricity']}  ガス: {d['last_gas']}"
        )