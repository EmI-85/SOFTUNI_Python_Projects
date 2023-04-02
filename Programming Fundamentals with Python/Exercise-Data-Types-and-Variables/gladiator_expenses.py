lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_expenses = 0
shields_count = 0

for i in range(1, lost_fights_count + 1):
    if i % 2 == 0:
        total_expenses += helmet_price
    if i % 3 == 0:
        total_expenses += sword_price
    if i % 6 == 0:
        shields_count += 1
        total_expenses += shield_price
        if shields_count == 2:
            total_expenses += armor_price
            shields_count = 0

print(f"Gladiator expenses: {total_expenses:.2f} aureus")

