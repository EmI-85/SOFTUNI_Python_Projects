skumria_price = float(input())
caca_price = float(input())
palamud_kilos = float(input())
safrid_kilos = float(input())
midi_kilos = int(input())

palamud_price = skumria_price * 1.60
safrid_price = caca_price * 1.80
midi_price = 7.50

total_sum = palamud_price * palamud_kilos + safrid_price * safrid_kilos + midi_price * midi_kilos
print(f"{total_sum:.2f}")

