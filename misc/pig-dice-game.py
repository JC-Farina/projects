# dice game : rolls two die and outputs the result
# asks usr if they want to roll again
# optional: keep track of number of rolls
# Ask: roll die? and update counter
# generate ramdom ints for die numbers
# output results
import random

points = 0
target = int(input('how many points'))
gameOver = False

while not gameOver:
    choice = input("Roll dice? (y/n): ").lower()

    if points >= target:
        print('Game Over')
        gameOver = True

    elif choice == 'y':
        die = random.randint(1, 6)
        points += die
        print(f"{die} {points}")
    elif choice == 'n':
        gameOver = True
    else:
        print('Invalid command. Try again!')
