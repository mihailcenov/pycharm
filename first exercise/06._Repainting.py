# •	Предпазен найлон - 1.50 лв. за кв. метър
# •	Боя - 14.50 лв. за литър
# •	Разредител за боя - 5.00 лв. за литър
plastic = int(input())
paint = int(input())
liquid = int(input())
hours_to_work = int(input())

price_plastic = (plastic + 2) * 1.5
price_paint = (paint + paint * 0.10) * 14.50
#print(price_paint)
price_liquid = liquid * 5
price_materials = price_plastic + price_paint + price_liquid + 0.40
#print(price_materials)
price_workers = (price_materials * 0.30) * hours_to_work
#print(price_workers)
total_money = price_materials + price_workers
print(total_money)
