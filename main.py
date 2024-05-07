from datetime import datetime
import requests

LAT = 31.945368
LONG = 35.928371
PARAMS = {"lat": LAT, "lng": LONG, "formatted": 0}

response = requests.get("https://api.sunrise-sunset.org/json", params=PARAMS)
data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

now = str(datetime.now()).split(" ")[1].split(":")[0]

print(now)
