import csv
from pathlib import Path

CSV_DIR = Path(__file__).parent / "data"

META = {
    "通常": {
        "file": "normal_data.csv",
        "status": "normal",
        "title": "お元気です",
        "message": "いつも通りの生活リズムです",
        "last_electricity": "09:12",
        "last_gas": "08:47",
        "note": None,
    },
    "やや注意": {
        "file": "normal_data.csv",
        "status": "warning",
        "title": "やや注意が必要です",
        "message": "ここ数日、ガスの利用が少なめです。体調などに変化はありませんか？",
        "last_electricity": "09:12",
        "last_gas": "16:35",
        "note": "ガスの利用が少なめです（平常レンジ比 -60%）",
    },
    "異常": {
        "file": "abnormal_data.csv",
        "status": "alert",
        "title": "異常の可能性があります",
        "message": "電気の利用が24時間ありません。一方でガスが長時間使われています。ご連絡ください。",
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


def _baseline():
    _, electricity, _ = _read("normal_data.csv")
    upper = [round(v * 1.3, 3) for v in electricity]
    lower = [round(v * 0.7, 3) for v in electricity]
    return upper, lower


def get(scenario):
    meta = META[scenario]
    hours, electricity, gas = _read(meta["file"])

    if scenario == "やや注意":
        gas = [round(v * 0.4, 3) for v in gas]

    upper, lower = _baseline()

    return {
        "status": meta["status"],
        "title": meta["title"],
        "message": meta["message"],
        "updated_at": "2026/09/10 09:32",
        "hours": hours,
        "electricity": electricity,
        "gas": gas,
        "baseline_upper": upper,
        "baseline_lower": lower,
        "last_electricity": meta["last_electricity"],
        "last_gas": meta["last_gas"],
        "note": meta["note"],
    }


if __name__ == "__main__":
    d = get("異常")
    print(d["title"], len(d["electricity"]))