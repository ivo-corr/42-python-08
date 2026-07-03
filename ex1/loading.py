import importlib.util
from importlib.metadata import version
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
            print("\tInstall it with:\n\tpip install -r requirements.txt")
            ko = True
        else:
            print(f"[OK] {dname} ({version(dname)}) - {dmsg} ready")
    if (ko):
        exit()


def get_weather_forecast():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 48.7758,   # Stuttgart
        "longitude": 9.1829,
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
        "timezone": "Europe/Berlin"
    }
    response = requests.get(url, params=params)
    data = response.json()
    return (data["daily"])



def main():
    print("\nLOADING STATUS: Loading programs...\n")
    check_dependencies()
    print("\nAnalyzing Matrix data...")
    data = get_weather_forecast()
    # data = (np.arange(1000),
    #         np.random.rand(1000))
    print("Processing 1000 data points...")
    print("Generating visualization...")
    plt.plot(data["time"], data["temperature_2m_max"])
    plt.show()


if __name__ == "__main__":
    main()
