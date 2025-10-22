cities = ["Greece", "Milan", "Rome", "London", "Peru"]

print("Original list of cities:")
print (cities)

print("InFirst city in the list:", cities[0])
print ("Last city in the list:", cities [-1])

cities.append ("Rome")
print("InList after adding a city with append():")
print(cities)

cities. insert(2, "Sydney")
print ("InList after inserting a city at position 2 with insert():")
print(cities)

removed_city = cities.pop()
print(f"\nRemoved city with pop(): (removed_city)")
print ("List after pop():") 
print(cities)

cities.remove("Peru")
print ("InList alter removing 'Peru' with remove():")
print(cities)

print("\nList in alphabetical order with sorted():")
print (sorted(cities))