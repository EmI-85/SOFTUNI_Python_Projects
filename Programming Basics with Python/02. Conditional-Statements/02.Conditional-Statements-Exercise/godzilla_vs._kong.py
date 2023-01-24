budget = float(input())
count_actors = int(input())
price_per_costume = float(input())

decor = budget * 0.10
clothes_price = count_actors * price_per_costume

if count_actors > 150:
    clothes_price = clothes_price * 0.9

total_sum = decor + clothes_price
diff = abs(total_sum - budget)

if total_sum <= budget:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")