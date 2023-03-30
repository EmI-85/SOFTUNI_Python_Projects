people_num = int(input())
capacity = int(input())

courses_count = 0

while people_num > 0:
    courses_count += 1
    people_num -= capacity
print(courses_count)

