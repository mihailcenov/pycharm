country = input() # Russia", "Bulgaria" или "Italy")
item = input() # ribbon", "hoop" или "rope")
hard_of_the_task = 0.0
performance = 0.0

if country == "Russia":
    if item == "ribbon":
        hard_of_the_task = 9.100
        performance = 9.400
    elif item == "hoop":
        hard_of_the_task = 9.300
        performance = 9.800
    elif item == "rope":
        hard_of_the_task = 9.600
        performance = 9.000
elif country == "Bulgaria":
    if item == "ribbon":
        hard_of_the_task = 9.600
        performance = 9.400
    elif item == "hoop":
        hard_of_the_task = 9.550
        performance = 9.750
    elif item == "rope":
        hard_of_the_task = 9.500
        performance = 9.400
elif country == "Italy":
    if item == "ribbon":
        hard_of_the_task = 9.200
        performance = 9.500
    elif item == "hoop":
        hard_of_the_task = 9.450
        performance = 9.350
    elif item == "rope":
        hard_of_the_task = 9.700
        performance = 9.150

the_assessment = hard_of_the_task + performance
max_the_assessment = 20 - the_assessment
percent_to_win = (max_the_assessment / 20) * 100

print(f"The team of {country} get {the_assessment:.3f} on {item}.")
print(f"{percent_to_win:.2f}%")

