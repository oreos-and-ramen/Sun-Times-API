import requests

url = "https://api.open-meteo.com/v1/forecast"

# defaults are for Salt Lake City
def get_data(latitude=40.746216, longitude=-111.905396):
    params = {
        "latitude" : latitude,
        "longitude": longitude,
        "daily"    : "sunrise,sunset",
        "timezone" : "auto"
    }
    
    response = requests.get(url, params=params)
    data = response.json()

    return data
