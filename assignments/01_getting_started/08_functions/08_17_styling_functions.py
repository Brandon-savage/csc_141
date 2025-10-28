def make_sandwich(*items):
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")

make_sandwich("Ham", "Cheese")
make_sandwich("Bacon", "Lettuce", "Tomato")
make_sandwich("bacon", "Lettuce", "Tomate", "Mayo")