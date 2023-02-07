people_sum = int(input())
line_input = input()
sum_all_grades = 0
count_grades = 0

while line_input != "Finish":
    presentation_title = line_input
    current_grades_sum = 0

    for grade in range(1, people_sum + 1):
        current_grade = float(input())
        count_grades += 1
        sum_all_grades += current_grade
        current_grades_sum += current_grade
    avg_current_grades = current_grades_sum / people_sum
    print(f"{presentation_title} - {avg_current_grades:.2f}.")
    line_input = input()

avg_all_grades = sum_all_grades / count_grades
print(f"Student's final assessment is {avg_all_grades:.2f}.")
