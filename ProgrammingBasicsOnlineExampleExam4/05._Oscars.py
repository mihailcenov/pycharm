actor_name = input()
points_from_academy = float(input())
evaluators = int(input())

for _ in range(evaluators):

    evaluator_name = input()
    evaluators_points = float(input())

    additional_points = (len(evaluator_name) * evaluators_points) / 2
    points_from_academy += additional_points

    if points_from_academy > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {points_from_academy:.1f}!")
        break
else:
    needed_points = 1250.5 - points_from_academy
    print(f"Sorry, {actor_name} you need {needed_points:.1f} more!")
