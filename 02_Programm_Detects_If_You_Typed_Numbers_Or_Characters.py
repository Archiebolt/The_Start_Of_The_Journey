# With this small project I learned how to check what the user typed in the input
# So if he typed numbers where he supposed to type characters - the program will yell at user
# Then it will turn the loop to the beginning and do that over and over till the user types what he was asked for

name = input("What is your name?: ")  # Just asks a user to type their name

while True:  # This look turns on a function that proves if what the user typed is a number or not
    if name.isdigit():  # If this is a number, then it will ask the user to type his name again and prove it again
        print("Sorry, but you can't write a number here.\nWe asked you about your name!")
        name = input("What is your name?: ")
        if  name.isdigit():  # The second prove, if user typed number again, it will turn the loop to the beginning
            continue
    else:  # If user typed characters, then everything is ok and it will go on to another loop
        break

while True:  # This look asks to type the user's age and proves if user typed a characters or numbers
    age = input(f"{name}, how old are you?: ")
    if age.isdigit():  # If user typed numbers, then everything is ok!
        if int(age) <= 150:  # If user types more then 150 years, it will send him to the beginning of the loop
            print(f"Congratulations, {name}! You're {age} years old!")
            break
        else:
            print(f"{name}, you can't be that old! Type your real age!")
            continue
    else:  # If user typed characters it will turn on the loop from the beginning
        print("Sorry, but you cant write a characters here.\nWe asked you about your age!")
        continue
