exam_hour = int(input())
exam_minute = int(input())
hour_of_arrival = int(input())
minute_of_arrival = int(input())

exam_in_minutes = (exam_hour * 60) + exam_minute
arrive_in_minutes = (hour_of_arrival * 60) + minute_of_arrival

diff = (exam_in_minutes - arrive_in_minutes )

if diff < 0:
    print("Late")
    hours = abs(diff // 60)
    minutes = abs(diff % 60)
    if hours == 0:
        print(f"{minutes} minutes after the start")
    else:
        print(f"{hours}:{minutes:02d} hours after the start")
elif 0 <= diff <= 30:
    print(f"{diff} On time")
    if diff > 0:
        print(f"{diff} minutes before the start")
elif diff > 30:
    print("Early")
    hours = abs(diff // 60)
    minutes = abs(diff % 60)
    if hours == 0:
        print(f"{minutes} minutes before the start")
    else:
        print(f"{hours}:{minutes:02d} hours before the start")