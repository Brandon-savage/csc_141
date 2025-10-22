cities = {
    "Orlando": {
        "country": "united states",
        "population": "334,854",
        "fact": "Orlando is known as the Theme Park Capital of the World and is one of the most visited cities globally due to major attractions like Walt Disney World and Universal Orlando Resort."
    },
    "Dallas": {
        "country": "united states",
        "population": "1.3 million",
        "fact": " Dallas is the largest metropolitan are in the nation not on a navigable body of water."
    },
    "new york": {
        "country": "united states",
        "population": "8.5 million",
        "fact": "New York City is home to the Statue of Liberty."
    }
}

for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"Country: {info['country'].title()}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact']}")