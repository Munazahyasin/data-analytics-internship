import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

# Number of attempts allowed
attempts = 5

print("Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 100.")
print("You have 5 attempts to guess it.")

for i in range(attempts):
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("Congratulations! You guessed the correct number!")
        break
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

    print("Attempts remaining:", attempts - i - 1)

else:
    print("Sorry! You have used all your attempts.")
    print("The correct number was:", number)