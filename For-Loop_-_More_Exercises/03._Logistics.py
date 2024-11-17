number_cargo = int(input())
the_tonnage_of_the_cargo = 0
bus = 0
track = 0
train = 0

for _ in range(1, number_cargo + 1, 1):
    the_tonnage_of_the_cargo = int(input())
    if the_tonnage_of_the_cargo <= 3:
        bus = bus + the_tonnage_of_the_cargo
    elif 4 <= the_tonnage_of_the_cargo <= 11:
        track = track + the_tonnage_of_the_cargo
    else:
        train = train + the_tonnage_of_the_cargo
        #kакто предишната задача тярябва да е
total_cargo = bus + track + train
#print(total_cargo)
average_price = (bus * 200 + track * 175 + train * 120) / total_cargo

bus_percent = (bus / total_cargo) * 100
track_percent = (track / total_cargo) * 100
train_percent = (train / total_cargo) * 100
print(f"{average_price:.2f}")
print(f"{bus_percent:.2f}%")
print(f"{track_percent:.2f}%")
print(f"{train_percent:.2f}%")















