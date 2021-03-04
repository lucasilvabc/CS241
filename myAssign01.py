import random
from random import randint

print("Welcome to the number guessing game!")
the_seed_value = input("Enter random seed: ")
random.seed(the_seed_value)

guesses = 0
num = randint(1, 100)
play_again = 'yes'

while play_again == 'yes':
  guesses = 0
  guess = 0
  num = randint(1, 100)
  while guess != num:
    guess = int(input("\nPlease enter a guess: "))
    guesses = guesses + 1
    if guess < num:
      print("Higher")
    elif guess > num:
      print("Lower")
      
  print("Congratulations. You guessed it!")
  print("It took you", guesses, "guesses.") 
  play_again = input("Would you like to play again (yes/no)? ")
print("Thank you. Goodbye.")