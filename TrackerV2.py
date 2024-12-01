import requests

API_KEY = "gR2PhBYJZvrRXd2ieh9PZloVwph3Q5qvPSHDAAM3"
BASE_URL = "https://api.nasa.gov/neo/rest/v1/feed"

# Function to fetch asteroid data and display details
def fetchAsteroids(start_date, end_date):
    url = f"{BASE_URL}?start_date={start_date}&end_date={end_date}&api_key={API_KEY}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to retrieve data:", response.status_code)
        return

    data = response.json()
    near_earth_objects = data.get("near_earth_objects", {})

    for date, asteroids in near_earth_objects.items():
        print(f"\nAsteroids on {date}:\n")
        for asteroid in asteroids:
            name = asteroid.get("name")
            is_hazardous = isPotentiallyHazardousAsteroid(asteroid)
            diameter = biggerThan1km(asteroid)

            print("-----------")
            print(f"Name: {name}")
            print(f"Potentially Hazardous: {is_hazardous}")
            print(diameter)
            print("-----------\n")

            print("0-0-0-0-0-0-0-0-0-0-0-0\n")
            print(isPotentiallyHazardousAsteroid(asteroid))
            print(biggerThan1km(asteroid))
            print(findBiggestOnes)

# Helper function to determine if an asteroid is potentially hazardous
def isPotentiallyHazardousAsteroid(asteroid):
    return "Yes" if asteroid.get("is_potentially_hazardous_asteroid") else "No"

# Helper function to check if an asteroid is larger than 1 km
def biggerThan1km(asteroid):
    diameter_km = asteroid.get("estimated_diameter", {}).get("kilometers", {}).get("estimated_diameter_max", 0)
    if diameter_km > 1:
        return f"Bigger than 1km \nDiameter: {diameter_km} km"
    else:
        return f"Smaller than 1km \nDiameter: {diameter_km} km"

# Optional helper function to find asteroids larger than 20 km
def findBiggestOnes(asteroid):
    diameter_km = asteroid.get("estimated_diameter", {}).get("kilometers", {}).get("estimated_diameter_max", 0)
    if diameter_km > 20:
        return f"Bigger than 20km \nDiameter: {diameter_km} km"
    else:
        return f"Smaller than 20km \nDiameter: {diameter_km} km"

# Run the fetchAsteroids function
fetchAsteroids("2024-11-08", "2024-11-15")
