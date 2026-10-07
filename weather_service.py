import random
import json
import xml.etree.ElementTree as ET


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

def get_weather_data(city=None):
    """Return weather data for all cities or one selected city."""
    data = generate_weather_data()

    if city is None:
        return data

    matches = [
        weather for weather in data
        if weather["city"].lower() == city.lower()
    ]

    if not matches:
        raise ValueError(f"City '{city}' was not found.")

    return matches


def weather_to_json(weather_data):
    """Convert weather data to JSON format."""
    return json.dumps(weather_data, indent=4)

def weather_to_xml(weather_data):
    """Convert weather data to XML format."""
    root = ET.Element("weather")

    for weather in weather_data:
        city = ET.SubElement(root, "city")

        name = ET.SubElement(city, "name")
        name.text = weather["city"]

        temperature = ET.SubElement(city, "temperature")
        temperature.text = str(weather["temperature"])

        humidity = ET.SubElement(city, "humidity")
        humidity.text = str(weather["humidity"])

        condition = ET.SubElement(city, "condition")
        condition.text = weather["condition"]

    ET.indent(root, space="    ")

    return ET.tostring(root, encoding="unicode") 
   
if __name__ == "__main__":
    data = generate_weather_data()

    print(weather_to_json(data))
    print(weather_to_xml(data))
    print(weather_to_json(get_weather_data("Nairobi"))) 