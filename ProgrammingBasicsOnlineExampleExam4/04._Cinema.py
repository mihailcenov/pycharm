hall_capacity = int(input())
total_income = 0
seats_taken = 0


while True:
    command = input()
    if command == "Movie time!":
        seats_left = hall_capacity - seats_taken
        print(f"There are {seats_left} seats left in the cinema.")
        break

    people_entering_the_cinema = int(command)
    if seats_taken + people_entering_the_cinema > hall_capacity:
        print(f"The cinema is full.")
        break

    seats_taken += people_entering_the_cinema
    ticket_income = people_entering_the_cinema * 5
    if people_entering_the_cinema % 3 == 0:
        ticket_income -= 5

    total_income += ticket_income
print(f"Cinema income - {total_income} lv.")