divisor = int(input())
boundary = int(input())
max_multiplier = 0

for current_num in range(boundary, divisor, -1):
    if current_num % divisor == 0:
        max_multiplier = current_num
        break
print(max_multiplier)


