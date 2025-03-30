import datetime as dt
import requests
import json

base_url = "http://api.openweathermap.org/data/2.5/weather?"
api_key = input("Enter your API key: ")
city_name = input("Enter a city : ")
print(city_name)

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius,fahrenheit

url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])


print(f"Temperature in   {city_name}: {temp_celsius:.2f}°C or {temp_fahrenheit}°F")
print(f"Temperature in   {city_name} feels like: {feels_like_celsius:.2f}°C or {feels_like_fahrenheit}°F")      
print(f"Humidity in  {city_name}: {humidity}%")
print(f"Wind Speed in {city_name}: {wind_speed}m/s")
print(f"General Weather in {city_name}: {description}")
print(f"Sun Rises in {city_name} at {sunrise_time} local time.")
print(f"Sun Sets  in {city_name} at {sunset_time}  local time.")