inherited_money = float(input())
years_to_live = int(input())
ivan_years = 18
even_year_spendings = 12000

for age in range(1800, years_to_live + 1, 1):
    if age % 2 == 0:
        inherited_money -= even_year_spendings
        #age += 1
        ivan_years += 1
    elif age % 2 == 1:
        odd_year_spendings = 12000 + (50 * ivan_years)
        inherited_money -= odd_year_spendings
        ivan_years += 1
        #age += 1

if inherited_money >= 0:
    print(f"Yes! He will live a carefree life and will have {inherited_money:.2f} dollars left.")
elif inherited_money < 0:
    print(f"He will need {-inherited_money:.2f} dollars to survive.")












#
# let
# money = Number(input[0]);
# let
# lastYear = Number(input[1]);
# let
# age = 18;
# for (let year = 1800; year <= lastYear; year++) {
#         if (year % 2 === 0) {
#             money -= 12000;
#             age += 1;
#         } else {
#             money -= (12000 + (age * 50));
#             age += 1;
#         }
#     }
#     if (money >= 0
