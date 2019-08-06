import random

# This is just small program where you choose the number
# and computer tries to guess it without knowing the number


print("""
Well, you were always addicted to the games,
where the PC chooses the number and you
have to guess it right?

So NOW it is your turn to choose the number and
the computer tries to guess it! Go on!
""")

guess_number = int(input("Choose number between 1 and 100> "))
computer_number = 0
count_guess = 0
x = 100
y = 1


while computer_number != guess_number:
    computer_number = random.randint(y, x)
    count_guess += 1
    print(f"Computer> {computer_number}")
    if computer_number > guess_number:
        print("Computer, choose smaller number!")
        x = computer_number - 1
    elif computer_number < guess_number:
        print("Computer, choose bigger number!")
        y = computer_number

print(f"Computer won with {count_guess} tries!")
