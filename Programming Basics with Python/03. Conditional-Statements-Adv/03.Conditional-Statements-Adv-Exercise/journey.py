budget = float(input())
season = input()
destination = ""
trip_type = ""
costs = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        trip_type = "Camp"
        costs = budget * 0.30
    elif season == "winter":
        trip_type = "Hotel"
        costs = budget * 0.70
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        trip_type = "Camp"
        costs = budget * 0.40
    elif season == "winter":
        trip_type = "Hotel"
        costs = budget * 0.80
else:
    destination = "Europe"
    costs = budget * 0.90
    trip_type = "Hotel"

print(f"Somewhere in {destination}")
print(f"{trip_type} - {costs:.2f}")
