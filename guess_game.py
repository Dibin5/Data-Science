import random

secret_number = random.randint(1, 100)
attempt = 0
print("---3 chances games---")

while attempt < 3:
    guess = int(input(f"attempt{attempt + 1}: enter guess: "))
    attempt += 1

    if guess == secret_number:
        print("You Won!")
        break
    elif guess < secret_number:
        print("It is too Low")
    else:
        print("It is too High")

if guess != secret_number:
    print("\n---Bonus Chance!---")
    print("You lost, But I will give you ONE last try.")
    bonus_guess = int(input("enter the final bonus guess number: "))
    if bonus_guess == secret_number:
        print("You WON the GAME")
    else:
        print(f"Game Over, The secret number was: {secret_number}")
