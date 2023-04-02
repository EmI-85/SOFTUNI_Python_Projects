number_of_snowballs = int(input())
snowball_value = 0
best_snowball = 0
output_string = ""

for i in range(number_of_snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())

    snowball_value = ((weight // time) ** quality)

    if snowball_value > best_snowball:
        best_snowball = snowball_value
        output_string = f"{weight} : {time} = {best_snowball} ({quality})"
print(output_string)



