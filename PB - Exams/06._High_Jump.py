desired_height = int(input())
current_height = desired_height - 30
total_jumps = 0
failed_attempts = 0

while current_height <= desired_height:
    jump_height = int(input())
    total_jumps += 1
    if jump_height > current_height:
        if current_height == desired_height:
            print(f"Tihomir succeeded, he jumped over {current_height}cm after {total_jumps} jumps.")
            break
        current_height += 5
        failed_attempts = 0
    else:
        failed_attempts += 1
        if failed_attempts == 3:
            print(f"Tihomir failed at {current_height}cm after {total_jumps} jumps.")
            break




