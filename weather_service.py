import random
import json


CITIES = [
    "Nairobi",
    "London",
    "New York",
    "Tokyo",
    "Sydney",
]

CONDITIONS = [
    "sunny",
    "cloudy",
    "rainy",
]


def generate_weather_data():
    """Generate random weather data for the predefined cities."""
    weather_data = []

    for city in CITIES:
        weather = {
            "city": city,
            "temperature": random.randint(10, 35),
            "humidity": random.randint(30, 90),
            "condition": random.choice(CONDITIONS),
        }

        weather_data.append(weather)

    return weather_data


def weather_to_json(weather_data):
    """Convert weather data to JSON format."""
    return json.dumps(weather_data, indent=4)


if __name__ == "__main__":
    data = generate_weather_data()

    print(weather_to_json(data))