exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_all_min = (exam_hour * 60) + exam_minutes
arrival_all_min = (arrival_hour * 60) + arrival_minutes

diff = abs(arrival_all_min - exam_all_min)

if arrival_all_min > exam_all_min:
    print("Late")
    if diff < 60:
        print(f"{diff} minutes after the start")
    else:
        hour = diff // 60
        mins = diff % 60
        if mins < 10:
            print(f"{hour}:0{mins} hours after the start")
        else:
            print(f"{hour}:{mins} hours after the start")
elif arrival_all_min == exam_all_min or diff <= 30:
    print("On time")
    if 1 <= diff <= 30:
        print(f"{diff} minutes before the start")
else:
    print("Early")
    if diff < 60:
        print(f"{diff} minutes before the start")
    else:
        hour = diff // 60
        mins = diff % 60
        if mins < 10:
            print(f"{hour}:0{mins} hours before the start")
        else:
            print(f"{hour}:{mins} hours before the start")
