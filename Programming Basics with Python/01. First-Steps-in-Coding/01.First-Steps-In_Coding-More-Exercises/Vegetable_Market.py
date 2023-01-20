vegetable_price = float(input())
fruit_price = float(input())
vegatables_kg = int(input())
fruits_kg = int(input())

revenue_lv =vegetable_price * vegatables_kg + fruit_price * fruits_kg

revenue_eur = revenue_lv / 1.94
print(f"{revenue_eur:.2f}")

