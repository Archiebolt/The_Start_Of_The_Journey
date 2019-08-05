import random

count = 0
command = ""
random_number = random.randint(1, 100)


while random_number != command:
    command = int(input("Guess the number: "))
    if command > random_number:
        print("Less...")
    elif command < random_number:
        print("More...")
    else:
        break
    count += 1


print(f"You guessed the number with {count} tries!")