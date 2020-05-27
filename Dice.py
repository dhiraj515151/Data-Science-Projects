import random

from Tools.scripts.treesync import raw_input

min = 1
max = 6

roll_again = "yes"

while roll_again == "yes":
    print("Rolling the dices...")
    print("The values are....")
    print(random.randint(min, max))
    print(random.randint(min, max))

    roll_again = raw_input("Roll the dices again?")