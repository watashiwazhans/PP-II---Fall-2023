import random
name = input("Hello! What is your name?")
print("Well, KBTU, I am thinking of a number between 1 and 20.")
guessed_num = random.randint(1, 20)
guess = 0
num_guesses = 0
while guess != guessed_num:
    print("Take a guess")
    guess = int(input())
    num_guesses += 1
    if guess < guessed_num:
        print('Your guess is too low.')
    elif guess > guessed_num:
        print('Your guess is too high')
    else:
        print(f"Good job, {name}! You guessed my number in {num_guesses} guesses!")
        break