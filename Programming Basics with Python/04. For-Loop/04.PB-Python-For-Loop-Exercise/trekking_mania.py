group_num = int(input())
counter_Musala = 0
counter_Monblan = 0
counter_Kilimandjaro = 0
counter_K2 = 0
counter_Everest = 0
people_sum = 0

for i in range(1, group_num + 1):
    people_num = int(input())

    if people_num <= 5:
        counter_Musala += people_num
    elif 6 <= people_num <= 12:
        counter_Monblan += people_num
    elif 13 <= people_num <= 25:
        counter_Kilimandjaro += people_num
    elif 26 <= people_num <= 40:
        counter_K2 += people_num
    elif people_num > 40:
        counter_Everest += people_num
    people_sum += people_num

percentage_p1 = counter_Musala / people_sum * 100
percentage_p2 = counter_Monblan / people_sum * 100
percentage_p3 = counter_Kilimandjaro / people_sum * 100
percentage_p4 = counter_K2 / people_sum * 100
percentage_p5 = counter_Everest / people_sum * 100

print(f"{percentage_p1:.2f}%")
print(f"{percentage_p2:.2f}%")
print(f"{percentage_p3:.2f}%")
print(f"{percentage_p4:.2f}%")
print(f"{percentage_p5:.2f}%")
