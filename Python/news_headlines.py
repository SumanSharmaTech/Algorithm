import requests

# NewsAPI key (replace with your own)
api_key = "YOUR_API_KEY"

# Function to fetch news headlines
def get_news_headlines():
    base_url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": "us",  # Replace with the desired country code
        "apiKey": api_key,
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    headlines = [article["title"] for article in data["articles"]]
    return headlines

# Example usage
news_headlines = get_news_headlines()
# Display or send the news headlines
