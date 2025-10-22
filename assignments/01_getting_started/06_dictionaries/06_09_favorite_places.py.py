favorite_places = {
    "Brandon": ["Orlando", "New York", "San Jose"],
    "Autumn": ["London", "Rome", "Los Angles"],
    "Rico": ["Houston", "Pittsburg", "Austin"]}

for name, places in favorite_places.items():
    print(f"\n{name}'s favorite places are:")
    for place in places:
        print(f"- {place}")