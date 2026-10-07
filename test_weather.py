import json
import unittest
import xml.etree.ElementTree as ET

from weather_service import (
    CITIES,
    generate_weather_data,
    get_weather_data,
    weather_to_json,
    weather_to_xml,
)


class WeatherServiceTests(unittest.TestCase):

    def test_generates_all_cities(self):
        data = generate_weather_data()

        self.assertEqual(len(data), len(CITIES))
        self.assertEqual(
            {item["city"] for item in data},
            set(CITIES)
        )

    def test_json_output(self):
        data = generate_weather_data()
        result = json.loads(weather_to_json(data))

        self.assertEqual(len(result), len(CITIES))
        self.assertIn("city", result[0])
        self.assertIn("temperature", result[0])
        self.assertIn("humidity", result[0])
        self.assertIn("condition", result[0])

    def test_xml_output(self):
        data = generate_weather_data()
        result = weather_to_xml(data)

        root = ET.fromstring(result)

        self.assertEqual(root.tag, "weather")
        self.assertEqual(len(root.findall("city")), len(CITIES))

    def test_city_filter(self):
        data = get_weather_data("Nairobi")

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["city"], "Nairobi")

    def test_invalid_city(self):
        with self.assertRaises(ValueError):
            get_weather_data("Atlantis")


if __name__ == "__main__":
    unittest.main()