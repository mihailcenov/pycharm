period_of_time = int(input())
treated_patients = 0
untreated_patients = 0
doctors = 7
for period in range(1, period_of_time + 1):
    patients_per_day = int(input())
    if period % 3 == 0 and untreated_patients > treated_patients:
        doctors += 1


    if doctors >= patients_per_day:
        treated_patients += patients_per_day
    else:
        treated_patients += doctors
        untreated_patients += (patients_per_day - doctors)






print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")