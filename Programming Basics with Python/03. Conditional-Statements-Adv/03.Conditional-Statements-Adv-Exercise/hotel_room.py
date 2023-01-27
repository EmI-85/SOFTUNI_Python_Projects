month = input()
nights_num = int(input())
price_studio = 0
price_apartment = 0


if month == "May" or month == "October":
    price_studio = 50
    price_apartment = 65
    if 7 < nights_num <= 14:
        price_studio = 50 * 0.95
    elif nights_num > 14:
        price_studio = 50 * 0.70
elif month == "June" or month == "September":
    price_studio = 75.20
    price_apartment = 68.70
    if nights_num > 14:
        price_studio = 75.20 * 0.80
elif month == "July" or month == "August":
    price_studio = 76
    price_apartment = 77

if nights_num > 14:
    price_apartment = price_apartment * 0.90

total_price_studio = nights_num * price_studio
total_price_apartment = nights_num * price_apartment

print(f"Apartment: {total_price_apartment:.2f} lv.")
print(f"Studio: {total_price_studio:.2f} lv.")
