length = int(input())
width = int(input())
height = int(input())
percentage = float(input())

volume = length * width * height
volume_in_liters = volume / 1000

percentage_liters = volume_in_liters * (percentage / 100)
result = volume_in_liters - percentage_liters

print(result)