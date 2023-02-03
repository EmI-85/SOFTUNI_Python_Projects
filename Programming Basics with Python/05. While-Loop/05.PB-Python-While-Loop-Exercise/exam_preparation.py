poor_grades = int(input())
input_line = input()
grades_sum = 0
grades_count = 0
last_problem = ""
poor_grades_count = 0

while input_line != "Enough":
    last_problem = input_line
    current_grade = int(input())
    if current_grade <= 4:
        poor_grades_count += 1
    grades_sum += current_grade
    grades_count += 1

    if poor_grades_count >= poor_grades:
        break
    input_line = input()

if poor_grades_count >= poor_grades:
    print(f"You need a break, {poor_grades_count} poor grades.")
else:
    average_grade = grades_sum / grades_count
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {grades_count}")
    print(f"Last problem: {last_problem}")



