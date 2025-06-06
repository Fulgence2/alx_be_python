import requests

key = "fee480808cc4414198c154102250606"
city = "Nairobi"

weather_response = requests.get(url=f"https://api.weatherapi.com/v1/current.json?key={key}&q={city}&aqi=no")

print(weather_response)
print(weather_response.status_code)       # 200 (OK)
print(weather_response.text)              # Raw response body
print(weather_response.json())