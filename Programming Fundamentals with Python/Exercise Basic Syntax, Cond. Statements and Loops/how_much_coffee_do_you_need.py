command = input()
total_num_of_coffees = 0

while command != "END":
    if command == "coding" or command == "dog" or command == "cat" or command == "movie":
        total_num_of_coffees += 1
    elif command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
        total_num_of_coffees += 2
    command = input()

if total_num_of_coffees > 5:
    print("You need extra sleep")
else:
    print(total_num_of_coffees)
