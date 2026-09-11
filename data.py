import csv
from pathlib import Path

CSV_DIR = Path(__file__).parent / "data"

# 判定
NO_POWER_HOURS = 24
NIGHT_HOURS = [23, 0, 1, 2, 3, 4]
NIGHT_GAS_HOURS = 3


META = {
    "通常": {
        "file": "normal_data.csv",
        "status": "通常", 
        "last_electricity": "09:12",
        "last_gas": "08:47",
        "note": None,
    },
    "やや注意": {
        "file": "abnormal_data.csv",
        "status": "やや注意", 
        "last_electricity": "前日 19:32",
        "last_gas": "23:00",
        "note": None,
    },
    "異常": {
        "file": "abnormal_data.csv",
        "status": "異常", 
        "last_electricity": "前日 19:32",
        "last_gas": "23:00",
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


def _judge(hours, electricity, gas):
    #通常か異常か判定
    if _max_streak(electricity, lambda v: v == 0) >= NO_POWER_HOURS:
        return "異常"
    by_hour = {int(t.split(":")[0]): g for t, g in zip(hours, gas)}
    night = [by_hour.get(h, 0) for h in NIGHT_HOURS]
    if _max_streak(night, lambda v: v > 0) >= NIGHT_GAS_HOURS:
        return "異常"
    
    return "通常"


def get(scenario):
    meta = META[scenario]
    hours, electricity, gas = _read(meta["file"])

    return {
        "updated_at": "2026/09/10 09:32",
        "hours": hours,
        "electricity": electricity,
        "gas": gas,
        "last_electricity": meta["last_electricity"],
        "last_gas": meta["last_gas"],
        "note": meta["note"],
        "status": _judge(hours, electricity, gas), 
    }


if __name__ == "__main__":
    for name in META:
        d = get(name)
        print(name, "->", d["status"], "件数:", len(d["electricity"]))