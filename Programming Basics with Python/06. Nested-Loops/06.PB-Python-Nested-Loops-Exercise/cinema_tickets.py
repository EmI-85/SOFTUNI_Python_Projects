line_input = input()
total_count = 0
student_count = 0
standard_count = 0
kid_count = 0

while line_input != "Finish":
    movie_name = line_input
    capacity = int(input())
    command_line = input()
    current_movie_count = 0

    while command_line != "End":
        ticket_type = command_line
        total_count += 1
        current_movie_count += 1
        if ticket_type == "student":
            student_count += 1
        elif ticket_type == "standard":
            standard_count += 1
        elif ticket_type == "kid":
            kid_count += 1

        if current_movie_count == capacity:
            break
        command_line = input()

    percentage_current = current_movie_count / capacity * 100
    print(f"{movie_name} - {percentage_current:.2f}% full.")
    line_input = input()

print(f"Total tickets: {total_count}")

percentage_student = student_count / total_count * 100
print(f"{percentage_student:.2f}% student tickets.")
percentage_standard = standard_count / total_count * 100
print(f"{percentage_standard:.2f}% standard tickets.")
percentage_kids = kid_count / total_count * 100
print(f"{percentage_kids:.2f}% kids tickets.")