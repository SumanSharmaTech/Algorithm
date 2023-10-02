import requests

# They Said So Quotes API key (replace with your own)
api_key = "YOUR_API_KEY"

# Function to fetch the quote of the day
def get_quote_of_the_day():
    base_url = "https://quotes.rest/qod"
    params = {
        "category": "inspire",  # You can choose different categories
        "apiKey": api_key,
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    quote = data["contents"]["quotes"][0]["quote"]
    return quote

# Example usage
quote_of_the_day = get_quote_of_the_day()
# Display or send the quote of the day
