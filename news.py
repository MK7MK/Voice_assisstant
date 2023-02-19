import requests
from . import api
en='https://newsapi.org/v2/top-headlines?country=us&apiKey='+api.key
json_data=requests.get(en).json()

ar = []
def news():
    for i in range(3):
        ar.append('number'+str(i+1)+" "+json_data["article"][i]["title"]+".")
    return ar