n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(1, n + 1):
    current_num = int(input())
    if current_num < 200:
        p1 += 1
    elif current_num <= 399:
        p2 += 1
    elif current_num <= 599:
        p3 += 1
    elif current_num <= 799:
        p4 += 1
    elif current_num >= 800:
        p5 += 1

percentage_p1 = p1 / n * 100
percentage_p2 = p2 / n * 100
percentage_p3 = p3 / n * 100
percentage_p4 = p4 / n * 100
percentage_p5 = p5 / n * 100

print(f"{percentage_p1:.2f}%")
print(f"{percentage_p2:.2f}%")
print(f"{percentage_p3:.2f}%")
print(f"{percentage_p4:.2f}%")
print(f"{percentage_p5:.2f}%")
