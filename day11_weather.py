import requests
from datetime import datetime


def get_weather(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,weather_code"
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=5
        )

        response.raise_for_status()

        data = response.json()

    except requests.Timeout:
        print("Request timed out. Please try again.")
        return

    except requests.ConnectionError:
        print("Could not connect to the weather server.")
        return

    except requests.HTTPError:
        print("The weather API returned an error.")
        return

    except requests.RequestException:
        print("Something went wrong while contacting the API.")
        return

    current = data["current"]

    time = datetime.fromisoformat(current["time"])
    temperature = current["temperature_2m"]
    weather_code = current["weather_code"]

    weather_descriptions = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast"
    }

    weather = weather_descriptions.get(
        weather_code,
        "Unknown weather"
    )

    return {
    "weather": weather,
    "time": time.strftime("%I:%M %p"),
    "temperature": temperature
}


result= get_weather(23.2599, 77.4126)
print(result)