import random
lottery_tickets = []
for num in range(100):
    lottery_tickets.append(random.randrange(1000000000,9999999999))
t = random.sample(lottery_tickets, 2)
print(t)
