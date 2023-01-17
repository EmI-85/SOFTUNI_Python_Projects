price_per_sq_m = 7.61
discount_percentage = 0.18
sq_m_area = float(input())

total_price = sq_m_area * price_per_sq_m
discount_sum = total_price * discount_percentage
final_price = total_price - discount_sum

print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount_sum} lv.")