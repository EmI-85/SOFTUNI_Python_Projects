pages = int(input())
pages_per_hour = int(input())
days = int(input())

reading_hours = pages // pages_per_hour
hours_per_day = reading_hours // days

print(hours_per_day)
