import math

easter_bread = int(input())
total_sugar = 0
total_flour = 0
max_sugar = 0
max_flour = 0

for _ in range(easter_bread):
    sugar = int(input())
    flour = int(input())

    total_sugar += sugar
    total_flour += flour

    if sugar > max_sugar:
        max_sugar = sugar
    if flour > max_flour:
        max_flour = flour

sugar_packs = total_sugar / 950
flour_packs = total_flour / 750

print(f"Sugar: {math.ceil(sugar_packs)}")
print(f"Flour: {math.ceil(flour_packs)}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")

