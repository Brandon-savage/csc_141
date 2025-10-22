favorite_languages = [
     "Autumn""python",
    "Brandon""c",
    "Brandis""ruby",
    "Bj""python"]


people_to_poll = ["Autumn", "Brandon", "Brandis", "Bj", "John"]

for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you for taking the poll, {person.title()}!")
    else:
        print(f"{person.title()}, please take our poll!")