import random

secret = random.randint(1, 100)
guess = 0
attempts = 0

print(secret) 

while guess != secret:
    guess = int(input("Guess the number (1-100): "))
    attempts += 1
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"Congratulations! You've guessed the number {secret} in {attempts} attempts.")