from random import choice


lottery_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']


winning_ticket = []
for _ in range(4):
    winning_ticket.append(choice(lottery_values))

print("Any ticket matching these four numbers or letters wins a prize:")
print(winning_ticket)