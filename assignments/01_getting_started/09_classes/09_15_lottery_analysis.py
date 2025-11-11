from random import choice

lottery_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

winning_ticket = [choice(lottery_values) for _ in range(4)]
my_ticket = [1, 2, 3, 'A']  
attempts = 0

while True:
    attempts += 1
    drawn = [choice(lottery_values) for _ in range(4)]
    if drawn == my_ticket:
        break

print("Winning ticket:", winning_ticket)
print("Your ticket:", my_ticket)
print(f"It took {attempts} tries to win the lottery!")