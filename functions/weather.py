import requests
import json

key = "fee480808cc4414198c154102250606"
city = input("Enter your current city: ")

weather_response = requests.get(url=f"https://api.weatherapi.com/v1/current.json?key={key}&q={city}&aqi=no")

#Json response body
data = weather_response.json()
print(json.dumps(data, indent=4))