import requests

url = "https://www.boredapi.com/api/activity/"
response = requests.get(url)
activity = response.json()
print(activity)