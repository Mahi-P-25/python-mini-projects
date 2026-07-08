import random

print("=" * 30)
print("     GuessMaster")
print("=" * 30)

print("\nChoose Difficulty")
print("1. Easy")
print("2. Medium")
print("3. Hard")

choice = input("\nEnter your choice (1-3): ")

if choice == "1":
    limit = 50
    attempts = 10
elif choice == "2":
    limit = 100
    attempts = 8
elif choice == "3":
    limit = 500
    attempts = 7
else:
    print("Invalid choice. Medium difficulty selected.")
    limit = 100
    attempts = 8

secret = random.randint(1, limit)

print(f"\nI'm thinking of a number between 1 and {limit}.")
print(f"You have {attempts} attempts.\n")

for i in range(attempts):
    try:
        guess = int(input(f"Attempt {i + 1}/{attempts}: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if guess == secret:
        print(f"\n🎉 Correct! You guessed the number in {i + 1} attempts.")
        break

    if guess > secret:
        print("Too high!")
    else:
        print("Too low!")

    difference = abs(secret - guess)

    if difference <= 5:
        print("Hint: You're very close!")
    elif difference <= 15:
        print("Hint: Getting closer.")
    else:
        print("Hint: Not even close.")

else:
    print(f"\nGame Over! The number was {secret}.")

play_again = input("\nPlay again? (y/n): ")

if play_again.lower() == "y":
    print("Run the program again to play!")
else:
    print("Thanks for playing!")
