import random as r # module
import time as t
guesstimes = 0
while True:
  number = r.randint(0, 100)
  time1 = int(t.time())
  while True:
    guess = int(input("Enter a number between 0 and 100: "))
    if guess == number:
      print("You guessed right!")
      guesstimes += 1
      break
    elif guess > number:
      print("Your guess was too high. Guess   again!")
      guesstimes += 1
    elif guess < number:
      print("Your guess was too low. Guess  again!")
      guesstimes += 1
    else:
      print("Invalid input, guess again.")
      guesstimes += 1
  time2 = int(t.time())
  time3 = time2 - time1
  print("It took you", guesstimes, "guesses.")
  print("The number was", number, ".")
  print("It took you", time3, "seconds.")
  break
