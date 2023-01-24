import math
movie_name = input()
movie_duration = int(input())
break_duration = int(input())

lunch_time = break_duration / 8
rest_time = break_duration / 4

residual_time = break_duration - lunch_time - rest_time
diff = math.ceil(abs(residual_time - movie_duration))

if residual_time >= movie_duration:
    print(f"You have enough time to watch {movie_name} and left with {diff} minutes free time.")
else:
    print(f"You don't have enough time to watch {movie_name}, you need {diff} more minutes.")
