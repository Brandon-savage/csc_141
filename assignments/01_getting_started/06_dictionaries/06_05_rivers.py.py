rivers = {
    "Susquehanna": "united states",
    "colorado": "united states",
    "mississippi": "united states"
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nRivers mentioned:")
for river in rivers.keys():
    print(river.title())

print("\nCountries mentioned:")
for country in rivers.values():
    print(country.title())