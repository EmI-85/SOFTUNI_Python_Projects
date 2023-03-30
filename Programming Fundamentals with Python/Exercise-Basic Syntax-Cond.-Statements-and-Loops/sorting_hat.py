name = input()
is_sorted = False

while name != "Welcome!":
    if name == "Voldemort":
        print("You must not speak of that name!")
        is_sorted = False
        break

    if len(name) < 5:
        is_sorted = True
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        is_sorted = True
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        is_sorted = True
        print(f"{name} goes to Ravenclaw.")
    elif len(name) > 6:
        is_sorted = True
        print(f"{name} goes to Hufflepuff.")
    name = input()

if is_sorted:
    print("Welcome to Hogwarts.")

