import random

number = random.randint(1, 100)
guess = None
tries = 0

print("Guess the number (1–100)")

while guess != number:
    guess = int(input("Your guess: "))
    tries += 1

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")

print(f"Correct! You guessed it in {tries} tries.")
