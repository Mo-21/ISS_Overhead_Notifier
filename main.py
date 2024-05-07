from datetime import datetime
import requests

# My Longitude & Latitude
LAT = 31.945368
LONG = 35.928371


def is_iss_overhead():
    # Get ISS location
    res = requests.get("http://api.open-notify.org/iss-now.json")
    res.raise_for_status()
    iss_data = res.json()

    iss_lat = float(iss_data["iss_position"]["latitude"])
    iss_long = float(iss_data["iss_position"]["longitude"])

    # Check distance
    if LAT-5 <= iss_lat <= LAT+5 and LONG-5 <= iss_long <= LONG+5:
        return True


def is_night():
    # Get Sunrise and Sunset in Amman (local timezone)
    params = {"lat": LAT, "lng": LONG, "formatted": 0}

    response = requests.get("https://api.sunrise-sunset.org/json", params=params)
    response.raise_for_status()
    data = response.json()

    sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

    now = str(datetime.now()).split(" ")[1].split(":")[0]

    if sunset <= now <= sunrise:
        return True


if is_night() and is_iss_overhead():
    print("Hello")


