topping = ""

while topping != "quit":
    topping = input("Enter a pizza topping (or 'quit' to stop): ")
    if topping != "quit":
        print(f"I'll add {topping} to your pizza.")