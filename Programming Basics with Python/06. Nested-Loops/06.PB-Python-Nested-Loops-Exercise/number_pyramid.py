n = int(input())
current_num = 1
num_finished = False
for row in range(1, n + 1):
    for column in range(1, row + 1):
        if current_num > n:
            num_finished = True
            break
        print(current_num, end = " ")
        current_num += 1
    if num_finished:
        break
    print()