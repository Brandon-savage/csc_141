person1 = {
    "first_name": "Rico",
    "last_name": "Hall",
    "age": 19,
    "city": "baltimore "
}

person2 = {
    "first_name": "Autunm",
    "last_name": "Smith",
    "age": 18,
    "city": "baltimore"
}

person3 = {
    "first_name": "Andrew",
    "last_name": "brooks",
    "age": 18,
    "city": "baltimore"
}

people = [person1, person2, person3]

for person in people:
    print(f"Name: {person['first_name']} {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}\n")