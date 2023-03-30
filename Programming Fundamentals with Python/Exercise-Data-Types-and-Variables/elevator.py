people_num = int(input())
capacity = int(input())

courses_count = 0

while people_num > 0:
    if people_num > capacity:
        courses_count += 1
        people_num -= capacity
    else:
        courses_count += 1
        people_num -= people_num
print(courses_count)

