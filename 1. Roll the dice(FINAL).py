start = input("The computer will roll an average dice and you have to guess the number! Are you ready? (y/n) ")
if start == "y":
    import random
#random integer from 1-6
    secret = random.randint(1,6)
    secret_guess = int(input("What's your guess!"))
    while secret_guess != secret:
        secret_guess = int(input("What's your guess!"))
    if secret_guess == secret:
        print("WELL DONE! You've got it!")
    secret_guess += 1