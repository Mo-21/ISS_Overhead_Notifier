import requests

LAT = 31.945368
LONG = 35.928371
PARAMS = {"lat": LAT, "lng": LONG}

response = requests.get("https://api.sunrise-sunset.org/json", params=PARAMS)
data = response.json()

print(data)
