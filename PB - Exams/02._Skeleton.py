race_minutes = int(input())
race_seconds = int(input())
trace_in_meters = float(input())
seconds_per_100_meters = int(input())

record_time_in_seconds = (race_minutes * 60) + race_seconds
reduced_time_in_seconds = trace_in_meters / 120
total_reduced_time_in_seconds = reduced_time_in_seconds * 2.5
marin_time = (trace_in_meters / 100) *  seconds_per_100_meters - total_reduced_time_in_seconds

if marin_time <= record_time_in_seconds:
    print(f"Marin Bangiev won an Olympic quota!")
    print(f"His time is {marin_time:.3f}.")
else:
    needed_time = record_time_in_seconds - marin_time
    print(f"No, Marin failed! He was {-needed_time:.3f} second slower.")