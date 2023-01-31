import sys
n = int(input())
max_num = -sys.maxsize
total_sum = 0

for i in range(1, n + 1):
    current_num = int(input())
    total_sum += current_num
    if current_num > max_num:
        max_num = current_num
residual_sum = total_sum - max_num

if residual_sum == max_num:
    print("Yes")
    print(f"Sum = {residual_sum}")
else:
    diff = abs(residual_sum - max_num)
    print("No")
    print(f"Diff = {diff}")
