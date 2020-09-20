import json
import urllib.request
from WeatherObject import WeatherObject
from config import weather_api_key

def forecast():
    key = weather_api_key
    city_id = "2706003"
    unit = "metric"
    href = f"https://api.openweathermap.org/data/2.5/weather?id={city_id}&units={unit}&appid={key}"
    
    with urllib.request.urlopen(href) as url:
        data = json.loads(url.read().decode())
    weather = WeatherObject(data["main"]["temp"], data["main"]["temp_max"], data["main"]["temp_min"], data["weather"][0]["description"])
    
    return weather
