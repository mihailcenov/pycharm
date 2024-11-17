from math import pi

price_trip = float(input())
number_puzzles = int(input())
number_dolls = int(input())
number_bears = int(input())
number_small_toys = int(input())
number_tracks = int(input())

price_puzzles = number_puzzles * 2.60
price_dolls = number_dolls * 3
price_bears = number_bears * 4.10
price_small_toys = number_small_toys * 8.20
price_tracks = number_tracks * 2

price_toys = price_puzzles + price_dolls + price_bears + price_small_toys + price_tracks
#print(f"{total_price:.2f}")
number_toys = number_puzzles + number_dolls + number_bears + number_small_toys + number_tracks

discount_price = 0

if number_toys >= 50:
    discount_price = price_toys * 0.25
    #print(discount_price)

final_price = price_toys - discount_price
tax_fee = final_price * 0.10
#print(tax_fee)
profit = final_price - tax_fee

if profit >= price_trip:
    left_money = profit - price_trip
    print(f"Yes! {left_money:.2f} lv left.")
else:
    money_needed = price_trip - profit
    print(f"Not enough money! {money_needed:.2f} lv needed.")

fruits = ['apple', 2, 'orange', 3, 'plums', ['x', 'y', 'z'], 'raspberry']

for fruit in fruits:
    print(f"This fruit is {fruit}")

print(pi)

dact = {}
dact['aaa'] = 123
dact['bbb'] = 987

print(f"{dact['aaa']} ... {dact['bbb']}")

address = {}
address['town'] = 'Sofia'
address['street'] = 'Slivnica'
address['number'] = 121

print(f"address = {address}")

for key, value in address.items():
    print(f'Key: {key}, Value: {value}')

print('------------------------------')
# List of dictionaries
dict_list = [
    {'name': 'Alice', 'age': 25, 'city': 'New York'},
    {'name': 'Bob', 'age': 30, 'city': 'Los Angeles'},
    {'name': 'Charlie', 'age': 35, 'city': 'Chicago'}
]

# Loop through each dictionary in the list
for dictionary in dict_list:
    # Loop through each key-value pair in the dictionary
    for key, value in dictionary.items():
        print(f'{key}: {value}')
    print('---')  # Separator between dictionaries

print('------------------------------------------------')

# We define a nested dictionary (a dictionary inside another dictionary).
nested_dict = {
    'person1': {  # This is the first key in the outer dictionary
        'name': 'Alice',  # Key-value pair inside the inner dictionary
        'age': 25,
        'address': {  # The value of the 'address' key is another dictionary (a sub-dictionary)
            'city': 'New York',
            'zip_code': '10001'
        }
    },
    'person2': {  # This is the second key in the outer dictionary
        'name': 'Bob',
        'age': 30,
        'address': {  # Another sub-dictionary for the 'address' key
            'city': 'Los Angeles',
            'zip_code': '90001'
        }
    }
}

# Start a loop to go through each key-value pair in the outer dictionary.
for person, details in nested_dict.items():
    # 'person' is the key (e.g., 'person1', 'person2'), and 'details' is the value (which is another dictionary).
    print(f'Person: {person}')

    # Loop through the inner dictionary (details) to access its key-value pairs.
    for key, value in details.items():
        # Check if the value is a dictionary using isinstance() function.
        # This tells us if the current value is another dictionary (sub-dictionary).
        if isinstance(value, dict):
            # If the value is a dictionary, print the key and indicate that its value is more complex.
            print(f'  {key}:')

            # Loop through the sub-dictionary to access its key-value pairs.
            for sub_key, sub_value in value.items():
                # 'sub_key' and 'sub_value' represent the keys and values of the sub-dictionary.
                print(f'    {sub_key}: {sub_value}')
        else:
            # If the value is not a dictionary, print it directly.
            print(f'  {key}: {value}')

    # Print a separator line to indicate the end of the current person's data.



    print('---')  # Separator between persons

    # Create a Python array
    my_array = ['a', 'b', 'c', 'd', 'e']

    # Use a for loop to print the array
    ix = 0
    for item in my_array:
        print(f"Loop {ix} -> Now the item is {item}")
        ix = ix + 1

    print('----------------------------------------')

    for i in range(5):
        print(f"Loop {i} -> Now the item is {my_array[i]}")

