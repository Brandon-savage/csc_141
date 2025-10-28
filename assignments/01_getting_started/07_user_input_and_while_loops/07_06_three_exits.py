while age != "quit":
    age = input("Enter your age (or 'quit' to stop): ")
    if age != "quit":
        age = int(age)
        if age < 5:
            print("Your ticket is free.")
        elif age <= 16:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")