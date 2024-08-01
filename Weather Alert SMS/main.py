import os
import requests
from twilio.rest import Client

API_KEY = os.environ.get("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
LATITUDE = 25.395969
LONGITUDE = 68.357773
ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
FROM_NO = os.environ.get("FROM_NO")
TO_NO = os.environ.get("TO_NO")


def get_weather_data(api_key, lat, lon):
    """Fetch weather data from OpenWeatherMap API."""
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key
    }
    try:
        response = requests.get(url=BASE_URL, params=params)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


def kelvin_to_celsius(kelvin_temp):
    """Convert temperature from Kelvin to Celsius."""
    return round(kelvin_temp - 273.15, 2)


def get_wind_description(wind_speed):
    """Return a description of the wind speed."""
    if wind_speed <= 1:
        return "no wind"
    elif wind_speed <= 7:
        return "light wind"
    elif wind_speed <= 24:
        return "moderate wind"
    else:
        return "strong wind"


def main():
    weather_data = get_weather_data(API_KEY, LATITUDE, LONGITUDE)
    if weather_data:
        weather = weather_data["weather"][0]["main"].lower()
        wind_speed = weather_data["wind"]["speed"]
        temp = kelvin_to_celsius(weather_data["main"]["temp"])
        wind_description = get_wind_description(wind_speed)
        msg = f"It is {weather} right now, with a temperature of {temp}°C, and {wind_description}."

        client = Client(ACCOUNT_SID, AUTH_TOKEN)

        message = client.messages.create(
            body=msg,
            from_=FROM_NO,
            to=TO_NO
        )

        print(message.status)


if __name__ == "__main__":
    main()
