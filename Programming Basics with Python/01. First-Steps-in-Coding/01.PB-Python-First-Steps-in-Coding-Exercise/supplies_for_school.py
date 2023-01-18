pens = int(input())
markers = int(input())
detergent = int(input())
discount_percentage = int(input())

total_sum = pens * 5.80 + markers * 7.20 + detergent * 1.20
discount = discount_percentage / 100 * total_sum
final_price = total_sum - discount

print(final_price)