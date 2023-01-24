trip_price= float(input())
puzzle_count = int(input())
dolls_count = int(input())
teddy_count = int(input())
minions_count = int(input())
trucks_count = int(input())

puzzle_price = 2.60
dolls_price = 3.00
teddy_price = 4.10
minions_price = 8.20
trucks_price = 2.00

total_sum = puzzle_price * puzzle_count + dolls_price * dolls_count + teddy_price * teddy_count + minions_price * minions_count + trucks_price * trucks_count

toys_count = puzzle_count + dolls_count + teddy_count + minions_count + trucks_count

if toys_count >= 50:
    total_sum = total_sum * 0.75

total_sum = total_sum * 0.9
diff = abs(total_sum - trip_price)

if total_sum >= trip_price:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")
