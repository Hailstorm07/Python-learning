import requests

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 23.2599,
    "longitude": 77.4126,
    "hourly": "temperature_2m"
}

response = requests.get(url, params=params)

print(response.status_code)

data = response.json()

hourly = data["hourly"]

times = hourly["time"]
temperatures = hourly["temperature_2m"]

weather_data = []

for time, temperature in zip(times, temperatures):
    weather_data.append({
        "time": time,
        "temperature": temperature
    })

print("\nFirst 5 weather records:")
print(weather_data[:5])

warm_hours = []

for time, temperature in zip(times, temperatures):
    if temperature > 25:
        warm_hours.append({
            "time": time,
            "temperature": temperature
        })

print("\nWarm hours:")
print(warm_hours)


cool_hours = []

for time, temperature in zip(times, temperatures):
    if temperature < 25:
        cool_hours.append({
            "time": time,
            "temperature": temperature
        })

print("\nCool hours:")
print(cool_hours)


average_temperature = sum(temperatures) / len(temperatures)

print(f"\nAverage temperature: {average_temperature} Celsius")