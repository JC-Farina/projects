# dice game : rolls two die and outputs the result
# asks usr if they want to roll again
# optional: keep track of number of rolls
# Ask: roll die? and update counter
# generate ramdom ints for die numbers
# output results
import random
counter = 0

while True:
    choice = input("Roll dice? (y/n): ").lower()

    if choice == 'y':
        counter += 1
        sides = int(input("How many sides?"))
        die1 = random.randint(1, sides)
        die2 = random.randint(1, sides)
        print(f"{die1, die2}")
        print(f"This is roll number {counter}!")
    elif choice == 'n':
        print(f"Thanks for playing! You rolled {counter} times with us!")
        break
    else:
        print('Invalid command. Try again!')
