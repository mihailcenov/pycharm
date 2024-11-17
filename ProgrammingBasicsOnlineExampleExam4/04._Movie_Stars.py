actors_budget = float(input())

while True:
    actors_names = input()
    if actors_names == "ACTION":
        print(f"We are left with {actors_budget:.2f} leva.")
        break
    if len(actors_names) > 15:
        actor_payment = 0.20 * actors_budget
    else:
        actor_payment = float(input())

    actors_budget -= actor_payment
    if actors_budget < 0:
        print(f"We need {abs(actors_budget):.2f} leva for our actors.")
        break



