nylon = int(input())
paint = int(input())
thinner = int(input())
worker_hours = int(input())

nylon_price = (nylon + 2) * 1.50
paint_price = (paint * 1.10) * 14.50
thinner_price = thinner * 5.0
bags_price = 0.40

sum_materials = nylon_price + paint_price + thinner_price + bags_price
sum_workers = (sum_materials * 0.30) * worker_hours

total_sum = sum_materials + sum_workers
print(total_sum)
