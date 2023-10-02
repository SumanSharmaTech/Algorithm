import requests

# Weather API key (replace with your own)
api_key = "YOUR_API_KEY"

# Function to fetch weather data for a location
def get_weather_data(location):
    base_url = "https://api.weather.com/data/v2.5/weather"
    params = {
        "q": location,
        "appid": api_key,
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

# Example usage
location = "New York, US"
weather_data = get_weather_data(location)
# Extract and display relevant weather information
