# •	Козунак  – 3.20 лв.
# •	Яйца –  4.35 лв. за кора с 12 яйца
# •	Курабии – 5.40 лв. за килограм
# •	Боя за яйца - 0.15 лв. за яйце
bread = int(input())
box_of_eggs = int(input())
sweets = int(input())

price_bread = bread * 3.20
price_box_of_eggs = box_of_eggs * 4.35
price_sweets = sweets * 5.40
paint_for_eggs = (box_of_eggs * 12) * 0.15
#print(paint_for_eggs)
total_price = price_bread + price_box_of_eggs + price_sweets + paint_for_eggs

print(f"{total_price:.2f}")