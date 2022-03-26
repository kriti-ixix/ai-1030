import requests

url = "http://api.openweathermap.org/data/2.5/weather?zip=10001,us&appid=d15e4f8bb247b53efc9e1861ed4c18e0"
response = requests.get(url)
output = response.json()
name = output['name']
main = output['weather'][0]['main']
description = output['weather'][0]['description']
print(name)
print(main)
print(description)