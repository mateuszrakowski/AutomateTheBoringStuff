"""
Prints the weather for a location from the command line.

Usage:
python getOpenWeather.py <city_name, 2-letter_country_code>

Returns:
str: Current weather and temperature.
"""

APPID = "YourOpenWeatherID"

import json, requests, sys, pprint


# Compute location from command line arguments
if len(sys.argv) < 2:
    sys.exit("Usage: python getOpenWeather.py <city_name, 2-letter_country_code>")
location = " ".join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API
url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={APPID}"
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable
weatherData = json.loads(response.text)

# Print weather description
print(f"Current weather in {location}:")
print(weatherData["weather"][0]["main"], "-", weatherData["weather"][0]["description"])
print("Temperature:", weatherData["main"]["temp"], "K")
