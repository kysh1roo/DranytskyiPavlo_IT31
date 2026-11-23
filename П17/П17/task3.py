import sys

import requests

AUTHOR = "Dranytskyi Pavlo, IT-31"
URL = "https://api.open-meteo.com/v1/forecast"
CITY, LAT, LON = "Lutsk", 50.75, 25.34


def main():
    params = {
        "latitude": LAT,
        "longitude": LON,
        "current": "temperature_2m,wind_speed_10m",
    }
    try:
        response = requests.get(URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        current = data["current"]
        units = data["current_units"]
        temp = current["temperature_2m"]
        wind = current["wind_speed_10m"]
    except (requests.RequestException, KeyError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    print(AUTHOR)
    print(
        f"{CITY} ({LAT}, {LON}): {temp} {units['temperature_2m']}, "
        f"wind {wind} {units['wind_speed_10m']}"
    )


if __name__ == "__main__":
    main()
