import importlib.util
from importlib.metadata import version
import sys
try:
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import requests
except ImportError:
    pass


def check_dependencies():
    print("Checking dependencies: ")
    ko = False
    dependencies = ["pandas Data manipulation",
                    "numpy Numerical computation",
                    "matplotlib Visualization",
                    "requests Network access"]
    for d in dependencies:
        dname = d.split(" ", 1)[0]
        dmsg = d.split(" ", 1)[1]
        if importlib.util.find_spec(dname) is None:
            print(f"[KO] '{dname}' not installed")

            ko = True
        else:
            print(f"[OK] {dname} ({version(dname)}) - {dmsg} ready")
    if (ko):
        print("\n[ERROR] Some dependencies are missing, "
              "\n\tinstall them with one of the following\n\tcommands:\n")
        if ("pypoetry" in sys.executable):
            print("\t* poetry install")
            print("\t* poetry add [package name]\n")
        else:
            print("\t* pip install -r requirements.txt")
            print("\t* pip install [package name]\n")
        exit()


def get_weather_forecast():
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": 49.1427,    # Heilbronn
        "longitude": 9.2109,
        "start_date": "2023-01-01",
        "end_date": "2026-07-01",
        "daily": "temperature_2m_max,temperature_2m_min",
        "timezone": "Europe/Berlin"
    }
    response = requests.get(url, params=params)
    data = response.json()
    return (data)


def plot(data):
    plt.figure(figsize=(20, 6))
    plt.plot(data["daily"]["time"], data["daily"]["temperature_2m_max"],
             label="Max temp", color="red")
    plt.plot(data["daily"]["time"], data["daily"]["temperature_2m_min"],
             label="Min temp", color="blue")
    plt.axvline("2024-01-01", color="gray", linestyle="--")
    plt.axvline("2025-01-01", color="gray", linestyle="--")
    plt.axvline("2026-01-01", color="gray", linestyle="--")
    plt.xticks(["2024-01-01", "2025-01-01", "2026-01-01"],
               ["2024", "2025", "2026"])
    plt.xlabel("Time")
    plt.ylabel("Temperature")
    plt.title("Daily temperature range in Heilbronn (Jan 2023 to Jul 2026)")
    plt.legend()
    plt.savefig("matrix_analysis.png")
    plt.show()


def main():
    print("\nLOADING STATUS: Loading programs...\n")
    check_dependencies()
    print("\nAnalyzing Matrix data...")
    data = get_weather_forecast()
    print("Processing 1000 data points...")
    print("Generating visualization...")
    plot(data)
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
