pet1 = {"animal": "Dog", "owner": "Brandon"}
pet2 = {"animal": "Turtle", "owner": "Autumn"}
pet3 = {"animal": "Seal", "owner": "Rico"}

pets = [pet1, pet2, pet3]

for pet in pets:
    print(f"{pet['owner']} owns a {pet['animal']}.")