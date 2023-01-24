record_in_seconds = float(input())
distance_in_meters = float(input())
time_for_1_meter = float(input())

delay = (distance_in_meters // 15) * 12.5

swimmer_time = distance_in_meters * time_for_1_meter + delay

if swimmer_time < record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {swimmer_time:.2f} seconds.")

else:
    diff = swimmer_time - record_in_seconds
    print(f"No, he failed! He was {diff:.2f} seconds slower.")