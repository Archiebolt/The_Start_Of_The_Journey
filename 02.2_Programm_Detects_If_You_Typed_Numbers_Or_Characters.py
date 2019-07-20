# This is pretty much the same program as the last one that proves what did user typed in input, but much smaller
# And it will yell at him, if he typed something that he wasn't asked for

while True:
    try:
        command = input("In what company you've been working in?: ")
        command = int(command)
        print("Sorry, but you need to enter a name of company, not just numbers!")
    except ValueError:  # if the ERROR appears it doesn't show me it in console, it takes the error as "True"
        break
print(f"Cool, so you're company that you working in is {command}? it's great!")