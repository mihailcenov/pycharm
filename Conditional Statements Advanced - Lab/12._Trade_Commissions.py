city_name = input()
sale = float(input())
commission = 0.0

if sale >= 0.0:
    CityFound = False
    if city_name == "Sofia":
        CityFound = True
        if 0 <= sale <= 500:
            commission = 5.0
        elif 500 < sale <= 1000:
            commission = 7.0
        elif 1000 < sale <= 10000:
            commission = 8.0
        else:
            commission = 12
    elif city_name == "Varna":
        CityFound = True
        if 0 <= sale <= 500:
            commission = 4.5
        elif 500 < sale <= 1000:
            commission = 7.5
        elif 1000 < sale <= 10000:
            commission = 10.0
        else:
            commission = 13.0
    elif city_name == "Plovdiv":
        CityFound = True
        if 0 <= sale <= 500:
            commission = 5.5
        elif 500 < sale <= 1000:
            commission = 8
        elif 1000 < sale <= 10000:
            commission = 12
        else:
            commission = 14.5
    if CityFound is True:
        total_money = sale * commission / 100
        print(f"{total_money:.2f}")
    else:
        print("error")
else:
    print("error")




