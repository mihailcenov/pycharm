anual_fee = int(input())

shoes = anual_fee *  0.60     #(1 - 40 / 100)
equip = shoes *  0.80         #(1 - 20 / 100)
ball = equip * 0.25                 #/ 4
acc = ball * 0.20                   #/ 5

total_money = anual_fee + shoes + equip + ball + acc
print(total_money)