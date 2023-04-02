number_of_lines = int(input())
sum = 0

for i in range(number_of_lines):
    input_char = input()
    ascii_value = ord(input_char)
    sum += ascii_value
print(f"The sum equals: {sum}")

