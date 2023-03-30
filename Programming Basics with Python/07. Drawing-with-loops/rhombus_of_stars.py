number = int(input())

for row in range(1, number + 1):
    for col in range(0, number - row):
        print(" ", end = "")
    print("*", end = "")
    for col in range(0, row - 1):
        print(" *", end = "")
    print()

for row in range(number, 0, - 1):
    for col in range(number - row, 0, - 1):
        print(" ", end = "")
    for col in range(row - 1, 0, - 1):
        print(" *", end = "")
    print()
