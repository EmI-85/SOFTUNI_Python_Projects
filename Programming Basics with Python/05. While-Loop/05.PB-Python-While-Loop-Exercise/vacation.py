money_needed = float(input())
money_available = float(input())
spending_days_count = 0
all_days = 0

while money_available < money_needed:
    if spending_days_count == 5:
        break
    command = input()
    money_transaction = float(input())
    all_days += 1

    if command == "spend":
        spending_days_count += 1
        money_available = money_available - money_transaction
        if money_available < 0:
            money_available = 0
    elif command == "save":
        spending_days_count = 0
        money_available = money_available + money_transaction

if spending_days_count == 5:
    print("You can't save the money.")
    print(all_days)
else:
    print(f"You saved the money for {all_days} days.")



