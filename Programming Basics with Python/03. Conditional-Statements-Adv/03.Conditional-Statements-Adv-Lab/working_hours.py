time = int(input())
day = input()
if 10 <= time <= 18:
    if day != "Sunday":
        print("open")
    else:
        print("closed")
else:
    print("closed")
