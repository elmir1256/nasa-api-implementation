import requests
from datetime import datetime, timedelta

API_KEY = "gR2PhBYJZvrRXd2ieh9PZloVwph3Q5qvPSHDAAM3"
BASE_URL = "https://api.nasa.gov/neo/rest/v1/feed"

list = []

def fetchAsteroids(start_date, end_date):

    def isPotentiallyHazardousAsteroid(asteroid):
     if asteroid.get("is_potentially_hazardous_asteroid"):
        return "Yes"
     else:
        return "No"

    def biggerThan1km(asteroid):
        if asteroid.get("estimated_diameter").get("kilometers").get("estimated_diameter_max") > 1:
            return "Bigger than 1km \n" + f"Diameter: {asteroid.get('estimated_diameter').get('kilometers').get('estimated_diameter_max')}"
        else:
            return "Smaller than 1km \n" + f"Diameter: {asteroid.get('estimated_diameter').get('kilometers').get('estimated_diameter_max')}"

    url = f"{BASE_URL}?start_date={start_date}&end_date={end_date}&api_key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    near_earth_objects = data.get("near_earth_objects", {})

    for date, asteroids in near_earth_objects.items():
        print(f"\nAsteroids on {date}:\n")
        for asteroid in asteroids:
            name = asteroid.get("name")
            is_potentially_hazardous_asteroid = asteroid.get(f"Is Hazardous: {isPotentiallyHazardousAsteroid(asteroid)}")
            diameter = biggerThan1km(asteroid)

            print()
            print("-----------")
            print(f"Name: {name}")
            print(f"Potentially Hazardous: {is_potentially_hazardous_asteroid}")
            print(f"{diameter}")
            print("-----------")
            print()


today = datetime.today()
tommorow = today + timedelta(days=1)

fetchAsteroids(today.strftime('%Y-%m-%d'), tommorow.strftime('%Y-%m-%d'))