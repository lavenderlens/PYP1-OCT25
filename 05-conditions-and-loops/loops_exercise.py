# Part 2 Loops
# In this exercise you will create a number guess game. It will prompt the user to guess the
# magic number between 1 and 10. If the user guesses correctly, it will print a winner
# message and exit. If the user guesses incorrectly, he/she will be prompted again. The user
# will be given three go's after which, if he/she has not guessed correctly the script will
# print a loser message.
# 1. Create a script named loops_exercise.py.
# 2. Import the random module as follows:
# import random
# 3. Declare and assign a variable that produces a random number in the range 1-10, as follows:
# magic_number = random.randint(1, 10)
# 4. Code a loop that iterates three times.
# 5. Inside the loop…
# a. Prompt the user to input a guess and capture it in a variable named
# user_guess.
# b. If the user's guess equals the magic number, print a winner message to the
# console and break out of the loop.
# c. If the user's guess does not equal the magic number, print an appropriate
# message, e.g. too low or too high.
# 6. If the loop exits normally, the user has not guessed correctly so print a suitable
# consolation message to the console.

# solution 1 Brad / Mike
# import random
 
# magic_number = random.randint(1, 10)
 
# Give the user three attempts to guess the magic number
# for attempt in range(1, 4):
#     user_guess = int(input(f"Attempt {attempt}/3 - Enter your guess (1-10): "))
 
#     if user_guess == magic_number:
#         print("Winner! You guessed the magic number.")
#         break
#     if user_guess < magic_number:
#         print("Too low. Try again.")
#     else:
#         print("Too high. Try again.")
# else:
#     # loop completed without a correct guess
#     print(f"Sorry — you didn't guess the number. It was {magic_number}.")

# solution 2 Ellis/Chris/Katy
# import random
# magic_number = random.randint(1, 10)
# print(magic_number)
# counter = 0
# while counter < 3:
#     user_guess = int(input("guess a number"))
#     counter+=1
#     print("Try number: ", counter)
#     if magic_number == user_guess:
#         print("Whey hey! Whos clever then")
#         break
#     else:
#         print("Try again")
# else:
#     print("The number was: ", magic_number)

# solution 3 Shaun/Becca/Owen
import random
 
magic_number = random.randint(1, 10)
print(magic_number)#testing
for attempt in range(0, 3):
    user_guess = int(input("Guess the magic number between 1 and 10: "))
    if user_guess < magic_number:
        print("Too low!")
    elif user_guess > magic_number:
        print("Too high!")
    else:
        print(f"Congratulations! You've guessed the magic number {magic_number} in {attempt} attempts.")
        break

else:
    print(f"Sorry, you've used all attempts. The magic number was {magic_number}.")
