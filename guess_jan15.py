import random

secretNumber = random.randint(1,20)

print('I\'m thinking of a number between 1 and 20')

print('Take a guess my friend.')

for chances in range(1,7): #Player has only 6 guesses


 try:
    guess = int(input())

    if guess > secretNumber:
        print('You\'re thinking high')
        print('Try again')
    elif guess < secretNumber:
        print('You\'re thinking low')
        print('Try again')
    else:
        break
 except:
     print('Enter a number smarty pants!!')

if guess == secretNumber:
    print('Good job!!, You guessed my number in '+str(chances)+' guesses.')
else:
    print('Nope, I was thinking of '+str(secretNumber))

