number_of_snowballs = int(input())
snowball_value = 0
best_snowball = 0

for i in range(number_of_snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())

    snowball_value = int((weight / time) ** quality)

    if snowball_value > best_snowball:
        best_snowball = snowball_value
        print(f"{weight} : {time} = {best_snowball} ({quality})")



