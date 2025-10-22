# 04_11_my_pizzas_your_pizzas.py

my_pizzas = ["pepperoni", "cheese", "meat lovers"]
friend_pizzas = my_pizzas[:]  # a copy

my_pizzas.append("bacon")
friend_pizzas.append("philly")

print("My pizzas:", my_pizzas)
print("Friend's pizzas:", friend_pizzas)