number_of_orders = int(input())
total_price = 0
for order in range(number_of_orders):
    capsule_price = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if capsule_price < 0.01 or capsule_price > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules_per_day < 1 or capsules_per_day > 2000:
        continue
    current_order_price = capsule_price * capsules_per_day * days
    total_price += current_order_price
    print(f"The price for the coffee is: ${current_order_price:.2f}")
print(f"Total: ${total_price:.2f}")


