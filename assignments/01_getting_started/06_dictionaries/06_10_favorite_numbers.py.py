favorite_numbers = {
    "Autumn": [17, 7, 33],
    "Brandon": [17, 33],
    "Rico": [26, 62, 67],
    "Andrew": [31],
    "Harry": [50,57, 55]}


for name, numbers in favorite_numbers.items():
    print(f"\n{name}'s favorite numbers are:")
    for number in numbers:
        print(f"- {number}")