group_size = int(input())
days = int(input())
coins = 0

for i in range(1, days + 1):
    coins += 50
    if i % 10 == 0:
        group_size -= 2
    if i % 15 == 0:
        group_size += 5

    coins -= 2 * group_size
    if i % 3 == 0:
        coins -= 3 * group_size
    if i % 5 == 0:
        coins += 20 * group_size
        if i % 3 == 0:
            coins -= 2 * group_size

coins_per_person = int(coins / group_size)
print(f"{group_size} companions received {coins_per_person} coins each.")


