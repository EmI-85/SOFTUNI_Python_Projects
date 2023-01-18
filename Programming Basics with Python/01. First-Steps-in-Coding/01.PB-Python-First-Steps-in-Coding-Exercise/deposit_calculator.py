deposit_amount = float(input())
deposit_term = int(input())
interest_rate = float(input())

interest_per_year = deposit_amount * (interest_rate / 100)
interest_per_month = interest_per_year / 12
total_sum = deposit_amount + interest_per_month * deposit_term

print(total_sum)
