guests = ['Mom','Dad','Wife']


for guest in guests:
    print(f"Hi {guest}, you are invited to the dorm!")

cantmakeit = "Dad"
print(f"\nunfortunately, {cantmakeit} can't make it to the dinner.\n")

index_to_replace = guests.index(cantmakeit)
guests[index_to_replace] = 'sister'

for guest in guests:
    print(f"Hi {guest}, you are invited to the party!")