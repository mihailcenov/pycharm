room_rent = int(input())

price_statuettes = room_rent - room_rent * 0.30
catering = price_statuettes - price_statuettes * 0.15
sound = catering / 2

total_price = room_rent + price_statuettes + catering + sound
print(f"{total_price:.2f}")