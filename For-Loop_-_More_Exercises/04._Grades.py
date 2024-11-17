number_students = int(input())
total_grades = 0
topstudents = 0
between_4_00_4_99 = 0
students_between_3_4 = 0
fail_students = 0
average = 0


for _ in range(number_students):
    grades_on_the_test = float(input())
    total_grades += grades_on_the_test

    if grades_on_the_test <= 2.99:
        fail_students += 1
    elif 3 <= grades_on_the_test <= 3.99:
        students_between_3_4 += 1
    elif 4 <= grades_on_the_test <= 4.99:
        between_4_00_4_99 += 1
    else:
         topstudents += 1

average = total_grades / number_students
top = topstudents / number_students * 100
between = between_4_00_4_99 / number_students * 100
between_3_4 = students_between_3_4 / number_students * 100
fail = fail_students / number_students * 100
print(f"Top students: {top:.2f}%")
print(f"Between 4.00 and 4.99: {between:.2f}%")
print(f"Between 3.00 and 3.99: {between_3_4:.2f}%")
print(f"Fail: {fail:.2f}%")
print(f"Average: {average:.2f}")









