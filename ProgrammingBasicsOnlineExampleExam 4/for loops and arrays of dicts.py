person0 = {
    "name": "georgi",
    "surname": "Petrov",
    "family": "Kocev",
    "address": "Kokiche, 5"
}

print(person0)

persons = [
    {
        "name": "georgi",
        "surname": "Petrov",
        "family": "Kocev",
        "address": "Kokiche, 5"
    },
    {
        "name": "Ivan",
        "surname": "Ivanov",
        "family": "Kocev",
        "address": "Lale, 5"
    },
    {
        "name": "Venci",
        "surname": "Jordanov",
        "family": "Ilchev",
        "address": "Lilia, 5"
    }
]

print ("-------------------------------\n")
#print(persons)


ix = 0
for person in persons:
    print(f"[{ix}] = {person}")
    ix += 1

print ("-------------------------------\n")

print(persons[0])
print("+++++++++++++++++++")
print(persons[1])
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxx")

print(f"len(persons) = {len(persons)}")
for ixx in range(len(persons)):
    print(f"persons[{ixx}] = {persons[ixx]}")

print("*************************************")

for ixx in range(len(persons)):
    print(f"Person No.{ixx}:")
    print(f"  name = {persons[ixx]['name']}")
    print(f"  surname = {persons[ixx]['surname']}")
    print(f"  family = {persons[ixx]['family']}")
    print(f"  address = {persons[ixx]['address']}")
    print("")

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

for ixx in range(len(persons)):
    print(f"Person No.{ixx}:")
    for key, value in persons[ixx].items():
        print(f"  {key}: {value}")
    print("")

print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

ixx = 0
for person in persons:
    print(f"Person No.{ixx}:")
    for key, value in person.items():
        print(f"  {key}: {value}")
    print("")
    ixx += 1