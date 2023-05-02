import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    count = 0
    while guess != random_number:
        count += 1
        guess = int(input(f"enter your guess, between 0 and {x}: "))
        if (guess == random_number):
            print("Your guess is correct")
            print(f"it took you {count} tries to guess the number")
            break
        elif (guess < random_number):
            print("Your guess is low")
        else:
            print("Your guess is high")


guess(10)
