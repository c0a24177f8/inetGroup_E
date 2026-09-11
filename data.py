import csv
from pathlib import Path

CSV_DIR = Path(__file__).parent / "data"

META = {
    "通常": {
        "file": "normal_data.csv",
        "status": "通常", 
        "last_electricity": "09:12",
        "last_gas": "08:47",
        "note": None,
    },
    "異常": {
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
        "status": meta["status"], 
    }


if __name__ == "__main__":
    for name in META:
        d = get(name)
        print(name, "->", d["status"], "件数:", len(d["electricity"]))