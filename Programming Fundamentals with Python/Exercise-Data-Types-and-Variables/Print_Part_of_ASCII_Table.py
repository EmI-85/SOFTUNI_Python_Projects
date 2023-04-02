start_value = int(input())
end_value= int(input())
current_char = ""

for i in range(start_value, end_value + 1):
    current_char = chr(i)
    print(current_char, end = " ")

