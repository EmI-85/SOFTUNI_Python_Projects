ticket_type = input()
row_num = int(input())
col_num = int(input())

all_seats = row_num * col_num
price = 0

if ticket_type == "Premiere":
    price = 12
elif ticket_type == "Normal":
        price = 7.50
elif ticket_type == "Discount":
        price = 5.0

total_price = all_seats * price
print(f"{total_price:.2f} leva")

