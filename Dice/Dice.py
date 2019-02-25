# Dice class

import random


class Dice:
    def __init__(self, how_many_dice):
        self.dice_list = []
        self.roll(how_many_dice)

    def roll(self, how_many_dice):
        while len(self.dice_list) < 6:
            roll_spool = ''
            while len(roll_spool) < how_many_dice:
                roll_spool += str(random.randint(1, 6))

            self.dice_list.append(roll_spool)

    def __str__(self):
        return str(self.dice_list)
