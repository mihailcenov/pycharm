day_of_the_week = input()
type_day = ""
if day_of_the_week == "Monday":
    type_day = "Working day"
elif day_of_the_week == "Tuesday":
    type_day = "Working day"
elif day_of_the_week == "Wednesday":
    type_day = "Working day"
elif day_of_the_week == "Thursday":
    type_day = "Working day"
elif day_of_the_week == "Friday":
    type_day = "Working day"
elif day_of_the_week == "Saturday":
    type_day = "Weekend"
elif day_of_the_week == "Sunday":
    type_day = "Weekend"
else:
    type_day = "Error"

print(type_day)
