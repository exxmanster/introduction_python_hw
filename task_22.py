import random

guesses_count = 10

print('Hello My friend! What is your name?')
user_name = input()
number = random.randint(1, 10)

print('Well, I Want to play a game with you  ' + user_name + ',  I am thinking of a number between 1 and 10! Can you Guess it?',\
      'For each mistake I will be cutting off one of your fingers')




while guesses_count < 20:
    print('Take a guess.') # There are four spaces in front of print.
    guess = input()
    guess = int(guess)

    guesses_count2 = guesses_count + 1


    if guess < number:
     print('Your guess is too low.') # There are eight spaces in front of print.

    if guess > number:
          print('Your guess is too high.')
    if guess == number:
       break

if guess == number:
        guesses_count2 = str(guesses_count2)
        print('Good job, ' + user_name + '! You guessed my number in ' + guesses_count2 + ' guesses!')
if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)