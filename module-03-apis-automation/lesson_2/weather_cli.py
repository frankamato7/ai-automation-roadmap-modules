import requests
import sys

def get_weather(lat, lon):
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        "&current_weather=true"
    )
    
    response = requests.get(url)
    data = response.json()
    return data["current_weather"]

def get_coordinates(city_name: str):
    """
    Look up latitude/longitude for a given city name using Open-Meteo geocoding.
    Returns (lat, lon) or None if not found.
    """
    url = (
        "https://geocoding-api.open-meteo.com/v1/search"
        f"?name={city_name}&count=1"
    )
    response = requests.get(url)
    data = response.json()

    results = data.get("results")
    if not results:
        return None

    first = results[0]
    return first["latitude"], first["longitude"]


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 weather_cli.py <city name>")
        return
    
    # Join all args so we support multi-word cities ("New York")
    city_input = " ".join(sys.argv[1:])
    
    coords = get_coordinates(city_input)
    if coords is None:
        print(f"Could not find coordinates for '{city_input}'.")
        return
    
    lat, lon = coords
    weather = get_weather(lat, lon)
    
    
    temp_c = weather["temperature"]
    wind = weather["windspeed"]
    
    print(f"Weather for {city_input.title()}:")
    print(f"  Temperature: {temp_c}°C")
    print(f"  Wind Speed:  {wind} km/h")

if __name__ == "__main__":
    main()
