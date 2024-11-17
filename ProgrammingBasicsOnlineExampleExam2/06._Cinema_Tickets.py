total_tickets = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0

while True:
    movie_name = input()
    if movie_name == "Finish":
        break
    free_seats = int(input())
    sold_tickets = 0

    while sold_tickets < free_seats:
        ticket_type = input()
        if ticket_type == "End":
            break
        elif ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1
        sold_tickets += 1

    total_tickets += sold_tickets
    percent_full = (sold_tickets / free_seats) * 100
    print(f"{movie_name} - {percent_full:.2f}% full.")

if total_tickets > 0:
    percent_student = (student_tickets / total_tickets) * 100
    percent_standard = (standard_tickets / total_tickets) * 100
    percent_kid = (kid_tickets / total_tickets) * 100
else:
    percent_student = percent_standard = percent_kid = 0

print(f"Total tickets: {total_tickets}")
print(f"{percent_student:.2f}% student tickets.")
print(f"{percent_standard:.2f}% standard tickets.")
print(f"{percent_kid:.2f}% kids tickets.")
