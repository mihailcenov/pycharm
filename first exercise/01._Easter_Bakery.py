
price_flour_for_a_kilo = float(input())
flour_kilos = float(input())
sugar_kilos = float(input())
box_of_eggs = int(input())
packets_ferment = int(input())

price_sugar = price_flour_for_a_kilo * 0.75
price_box_of_eggs = price_flour_for_a_kilo + (price_flour_for_a_kilo * 0.10)
price_packets_ferment = price_sugar * 0.20

flour = price_flour_for_a_kilo * flour_kilos
sugar = sugar_kilos * price_sugar
eggs = box_of_eggs * price_box_of_eggs
ferment = price_packets_ferment * packets_ferment

total_price = flour + sugar + eggs + ferment

print(f"{total_price:.2f}")

