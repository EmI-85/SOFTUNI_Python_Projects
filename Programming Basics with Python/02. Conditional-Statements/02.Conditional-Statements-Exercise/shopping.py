budget = float(input())
videocards_count = int(input())
processors_count = int(input())
ram_count = int(input())

videocards_sum = videocards_count * 250
processors_sum = processors_count * (videocards_sum * 0.35)
ram_sum = ram_count * (videocards_sum * 0.10)

total_price = videocards_sum + processors_sum + ram_sum

if videocards_count > processors_count:
    total_price = total_price * 0.85

diff = abs(budget - total_price)

if budget >= total_price:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")