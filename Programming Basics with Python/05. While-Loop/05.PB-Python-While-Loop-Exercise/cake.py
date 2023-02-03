width = int(input())
length = int(input())

total_pieces = width * length
input_line = input()
cake_finished = False

while input_line != "STOP":
    current_pieces = int(input_line)
    total_pieces -= current_pieces
    if total_pieces <= 0:
        cake_finished = True
        break
    input_line = input()

if cake_finished:
    print(f"No more cake left! You need {abs(total_pieces)} pieces more.")
else:
    print(f"{total_pieces} pieces are left.")