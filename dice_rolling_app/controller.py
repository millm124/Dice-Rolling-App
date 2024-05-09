from random import randint

def calculate_total(dice_rolled, operation, sides):
    total = 0
    dice_rolls = str("Rolls: ")

    if operation == str("Addition"):

        for i in range(dice_rolled):
            roll = randint(1, sides)
            dice_rolls = dice_rolls + str(roll) + str(" ")
            total = total + roll
           
    if operation == str("Multiplication"):

        total = 1

        for i in range(dice_rolled):
            roll = randint(1, sides)
            dice_rolls = dice_rolls + str(roll) + str(" ")
            total = total * roll

    return dice_rolls, total
       

