import math

tournaments_num = int(input())
starting_points = int(input())
result_points = 0
wins_count = 0
finals_count = 0
semi_finals_count = 0

for i in range(1, tournaments_num + 1):
    result = input()
    if result == "W":
        result_points += 2000
        wins_count += 1
    elif result == "F":
        result_points += 1200
    elif result == "SF":
        result_points += 720

total_points = starting_points + result_points
average = result_points / tournaments_num
wins_percentage = wins_count/ tournaments_num * 100

print(f"Final points: {total_points}")
print(f"Average points: {math.floor(average)}")
print(f"{wins_percentage:.2f}%")
