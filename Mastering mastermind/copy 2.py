from random import randint

print("In this program you will enter a number between 1 - 100."
      "\nAfter the computer will try to guess your number!")

number = 0

while number < 1 or number > 100:
    number = int(input("\n\nEnter a number for the computer to guess: "))
    if number > 100:
        print("Number must be lower than or equal to 100!")
    if number < 1:
        print("Number must be greater than or equal to 1!")

guess = randint(1, 100)

print("The computer takes a guess...", guess)

while guess != number:
    if guess > number:
        guess -= 1
        guess = randint(1, guess)
    else:
        guess += 1
        guess = randint(guess, 100)
    print("The computer takes a guess...", guess)

print("The computer guessed", guess, "and it was correct!")
