# rock paper scissor: take input for rock paper scissors (r/p/s)
# display both choices using emojis
# select and display winner
# ask to play again

import random

gameOver = False
compMode = False
enableCompetitive = ''
userChoice = ''
machineChoice = ['r', 's', 'p']
winNum = 0
loseNum = 0
tieNum = 0

# dictionary to convert str to emoji
emojiMap = {
    "r" : "🪨",
    "p" : "📄",
    "s" : "✂️",
    "exit" : "👋"
}

enableCompetitive = input('Enable Coompetitive? (y/n) (best 2 out of 3)')

try:
    if enableCompetitive == 'y':
        compMode = True
        print('Competitive enabled, Good Luck!')
    elif enableCompetitive == 'n':
        print('Casual mode enabled, Have Fun!')
except:
    gameOver = True
    print('not a valid input')

while not gameOver:

    if compMode == True:
        if loseNum == 3:
            gameOver = True
            print(f'Game Over! You lost!')
            break
        elif winNum == 3:
            gameOver= True
            print('Game Over, winner winner chicken dinenr!')
            break

    userChoice = input('Make your choice: rock, paper, scissor (r/p/s) : ')
    machineChoice = random.choice("r" "p" "s")

    if userChoice == 'exit':
        machineChoice = 'exit'

    try:
        print(f'You have chosen : {emojiMap[userChoice]}, We have chosen : {emojiMap[machineChoice]} the results are...')
    except:
        print(f'{userChoice} is not a valid input')

    if machineChoice == 'exit':
        gameOver = True
        print(f'Bye Bye, you have won {winNum} times , lost {loseNum} times and tied {tieNum} times!')

    elif userChoice == machineChoice:
        print(f'No winners!')
        tieNum += 1
    elif userChoice == 'r' and machineChoice != 'p':
        print(f'You won!')
        winNum += 1
    elif userChoice == 's' and machineChoice != 'r':
        print(f'You won!')
        winNum += 1
    elif userChoice == 'p' and machineChoice != 's':
        print(f'Your won!')
        winNum += 1
    else:
        print(f'You lose!')
        loseNum += 1

