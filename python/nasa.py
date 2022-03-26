import requests

url = "https://api.nasa.gov/planetary/apod?api_key=j5gF4XUkbTGJBpM2XOhxqwbcNZLTpeGjpivdFMzr"
response = requests.get(url)
output = response.json()
print(output)