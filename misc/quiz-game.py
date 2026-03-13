# ask player a bank of questions
gameOver = False
playerScore = 0

while not gameOver:
    playerAns = ''

    print('Question 1: What is the capital of France?' //
   "a) Paris" //
    "b) London" //
    "c) Rome")
    # take player coices
    playerAns = input('Your answer: ')
    # eval against answers
    if  playerAns == 'a':
        print('Correct!')
        playerScore =+ 1

    elif playerAns != 'a':
        gameOver = True
        print(f'Incorrect! Your score was: {playerScore}')

# output score
