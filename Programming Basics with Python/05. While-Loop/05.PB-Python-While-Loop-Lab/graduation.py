name = input()
current_class = 1
fails = 0
total_grades = 0
isExcluded = False
while current_class <= 12:
    current_grade = float(input())
    if current_grade < 4:
        fails += 1
        if fails >= 2:
            isExcluded = True
            break
    else:
        current_class += 1
        total_grades += current_grade
if isExcluded:
    print(f"{name} has been excluded at {current_class} grade")
else:
    average = total_grades / 12
    print(f"{name} graduated. Average grade: {average:.2f}")
