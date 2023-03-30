command = input()
new_string = ""

while command != "End":
    if command == "SoftUni":
        command = input()
        continue
    for letter in range(len(command)):
        new_string += command[letter]*2
    print(new_string)
    new_string = ""
    command = input()

