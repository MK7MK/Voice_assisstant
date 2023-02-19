
import requests
from . import api



api_addr='http://api.openweathermap.org/data/2.5/weather?q=vellore&appid='+api.key_weather
json_data=requests.get(api_addr).json()


def temp():
    tempp=round(json_data["main"]["temp"]-273,1)
    return tempp


def des():
    desc=json_data["weather"][0]["description"]
    return desc
##