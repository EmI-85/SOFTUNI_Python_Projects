age = int(input())
price_washing_machine = float(input())
toy_price = int(input())
counter_toys = 0
sum = 0
money = 10
brother_count = 0

for i in range(1, age + 1):
    if i % 2 != 0:
        counter_toys += 1
    else:
        brother_count += 1
        sum = sum + money
        money = money + 10

result = sum + (toy_price * counter_toys) - brother_count
diff = abs(result - price_washing_machine)

if result >= price_washing_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")