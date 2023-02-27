budget = float(input())
price_1kg_flour = float(input())
price_1pack_eggs = price_1kg_flour * 0.75
price_1liter_milk = price_1kg_flour * 1.25
number_of_loaves = 0
coloured_eggs_num = 0

bread_price = price_1kg_flour + price_1pack_eggs + (0.250 * price_1liter_milk)

while budget > bread_price:
    number_of_loaves += 1
    budget -= bread_price
    coloured_eggs_num += 3
    if number_of_loaves % 3 == 0:
        coloured_eggs_num -= number_of_loaves - 2

print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {coloured_eggs_num} eggs and {budget:.2f}BGN left.")

