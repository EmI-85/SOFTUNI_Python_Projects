days_num = int(input())
room_type = input()
feedback = input()
price = 0
nights_num = days_num - 1

if room_type == "room for one person":
    price = 18
    result = price * nights_num
    if feedback == "positive":
        result = result * 1.25
    else:
        result = result * 0.90
elif room_type == "apartment":
    price = 25
    result = price * nights_num
    if days_num < 10:
        result = result * 0.70
    elif 10 <= days_num <= 15:
        result = result * 0.65
    elif days_num > 15:
        result = result * 0.50
    if feedback == "positive":
        result = result * 1.25
    else:
        result = result * 0.90
elif room_type == "president apartment":
    price = 35
    result = price * nights_num
    if days_num < 10:
        result = result * 0.90
    elif 10 <= days_num <= 15:
        result = result * 0.85
    elif days_num > 15:
        result = result * 0.80
    if feedback == "positive":
        result = result * 1.25
    else:
        result = result * 0.90
print(f"{result:.2f}")
