guests = ["Mom", "Dad", "Wife"]

for guest in guests:
    print(f"Hi {guest}, you are invited to dinner at my place!")

cantmakeit = "Mom"
print(f"\nunfortunately, {cantmakeit} cant make it to the dinner.\n")

guests[guests.index(cantmakeit)]= "Sister"

for guest in guests:
    print(f"Hi {guest}, you are still invited to dinner at my place")

    print("\ngood news! i found a better dinner table, so more guest can come!\n")
    insertbegining = "grandma"
    insertmiddle = "grandpa"
    appended = "brother"
    guests.insert(0,insertbegining)
    guests.insert(2, insertmiddle)
    guests.append(appended)
    for guest in guests:
       print(f"Hi {guest}, you are invited to dinner at my place!")