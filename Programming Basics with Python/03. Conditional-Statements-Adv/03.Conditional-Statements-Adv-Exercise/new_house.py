flower_type = input()
flowers_num = int(input())
budget = int(input())
sum = 0

if flower_type == "Roses":
    sum = 5 * flowers_num
    if flowers_num > 80:
        sum = sum * 0.90
elif flower_type == "Dahlias":
    sum = 3.80 * flowers_num
    if flowers_num > 90:
        sum = sum * 0.85
elif flower_type == "Tulips":
    sum = 2.80 * flowers_num
    if flowers_num > 80:
        sum = sum * 0.85
elif flower_type == "Narcissus":
    sum = 3 * flowers_num
    if flowers_num < 120:
        sum = sum * 1.15
elif flower_type == "Gladiolus":
    sum = 2.50 * flowers_num
    if flowers_num < 80:
        sum = sum * 1.20

diff = abs(budget - sum)

if sum <= budget:
    print(f"Hey, you have a great garden with {flowers_num} {flower_type} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")

