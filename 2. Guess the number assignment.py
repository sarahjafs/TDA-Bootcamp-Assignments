import random

trials = 0

number = random.randint(1,20)
print("I am thinking of an integer between 1 and 20")

while trials < 21:
    print    ("What do you think it is?")
    guess = input()
    guess = int(guess)
    
    trials = trials + 1
    
    if guess < number:
        print("Too low!")
    
    elif guess > number:
        print("Too high!")
    
    elif guess == number:
        trials = str(trials)
        print("Well done you! You guessed the number I am thinking in " + trials + " tries!")
        break