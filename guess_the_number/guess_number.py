import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    count = 0
    while guess != random_number:
        count += 1
        guess = int(input(f"enter your guess, between 0 and {x}: "))
        if guess == random_number:
            print("Your guess is correct")
            print(f"it took you {count} tries to guess the number")
            break
        elif guess < random_number:
            print("Your guess is low")
        else:
            print("Your guess is high")


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(
            f"Is {guess} too high(H), too low(L), or correct (C)?: ").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"Yayyy, the computer guessed your number {guess},  correctly!!!!!")


computer_guess(13)
