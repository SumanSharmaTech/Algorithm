import requests

# Edamam Recipe Search API credentials (replace with your own)
app_id = "YOUR_APP_ID"
app_key = "YOUR_APP_KEY"

# Function to get a recipe of the day
def get_recipe_of_the_day():
    base_url = "https://api.edamam.com/search"
    params = {
        "q": "recipe of the day",
        "app_id": app_id,
        "app_key": app_key,
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    if "hits" in data:
        recipe = data["hits"][0]["recipe"]["label"]
        return recipe
    else:
        return "Recipe not found."

# Example usage
recipe_of_the_day = get_recipe_of_the_day()
# Display or send the recipe of the day
