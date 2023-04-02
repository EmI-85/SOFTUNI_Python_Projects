capacity = 255
num_of_lines = int(input())
water_in_tank = 0

for i in range(num_of_lines):
    quantity = int(input())
    if quantity + water_in_tank > capacity:
        print("Insufficient capacity!")
    else:
        water_in_tank += quantity
print(water_in_tank)


