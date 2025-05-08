import random

# List of South American countries
south_american_countries = [
    "Argentina", "Bolivia", "Brazil", "Chile", "Colombia",
    "Ecuador", "Guyana", "Paraguay", "Peru", "Suriname",
    "Uruguay", "Venezuela"
]

def random_country_selector():
    # Randomly select a country
    selected_country = random.choice(south_american_countries)
    print(f"The roulette selected: {selected_country}")

# Run the roulette
if __name__ == "__main__":
    random_country_selector()