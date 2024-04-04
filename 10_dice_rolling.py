import random

def roll_dice():
    dice_drawing = {
        1 : (
            " ___________ ",
            "|           |",
            "|     1     |",
            "|     *     |",
            "|___________|",
        ),
        2 : (
            " ___________ ",
            "|   *       |",
            "|     2     |",
            "|       *   |",
            "|___________|", 
        ),
        3 : (
            " ___________ ",
            "|     *     |",
            "|     3     |",
            "|   *   *   |",
            "|___________|",
        ),
        4 : (
            " ___________ ",
            "|  *    *   |",
            "|     4     |",
            "|  *    *   |",
            "|___________|",
        ),
        5 : (
            " ___________ ",
            "|  *    *   |",
            "|    5*     |",
            "|  *    *   |",
            "|___________|",
        ),
        6 : (
            " ___________ ",
            "|  *  *  *  |",
            "|     6     |",
            "|  *  *  *  |",
            "|___________|",
        )
    }
    roll = input("you want roll the dice ? (yes/no): ")


    while roll.lower() == "yes".lower():
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)

        print("dice rolled: {} and {}".format(dice1,dice2))
        #print("/n".join(dice_drawing[dice1]))
        #print("/n".join(dice_drawing[dice2]))
        
        roll = input("you want rolled again: (yes/no)? ")

roll_dice()