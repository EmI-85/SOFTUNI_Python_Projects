chicken_menu = int(input())
fish_menu = int(input())
veggie_menu = int(input())

price_chicken = chicken_menu * 10.35
price_fish = fish_menu * 12.40
price_veggie = veggie_menu * 8.15

price_menus_sum = price_chicken + price_fish + price_veggie
dessert_price = 0.20 * price_menus_sum

total_price = price_menus_sum + dessert_price + 2.5
print(total_price)