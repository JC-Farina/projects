# generate secret num
# ask for usr guess up to 3
# if correct print winner
# if not print try again
# if not number print error

import random

guessCount = 0
minNum = int(input('Select the minimum value to guess '))
maxNum = int(input('Select the maximum value to guess '))
secretNum = random.randint(minNum, maxNum)
gameOver = False

print(f'{secretNum}')

while not gameOver:
    usrGuess = int(input(f'Guess a number from {minNum} - {maxNum}! (Enter 0 to exit) '))
    guessCount += 1

    if usrGuess == 0:
        gameOver = True
    elif usrGuess == secretNum:
        print(f"Winner!! Great job the number was {secretNum}! and you guessed the number in {guessCount} attempts")
    elif usrGuess != secretNum:
        if usrGuess < secretNum:
            print(f"Try again {usrGuess} is too low")
        else:
            print(f'Try again {usrGuess} is too high')
    elif guessCount >=3:
        gameOver = True
        print(f'You lost! The correct number was {secretNum}')
    else:
        print("Not a valid option")
