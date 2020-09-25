import random

# Generate values between 0 and 1

# Random between numbers
for i in range(4):
    print(random.randint(1,2))

# choice() allow to
teammates = ("John", "Kat", "Sahra")
leaders = random.choice(teammates)
print(leaders)


class Dice:
    def roll(self):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        return dice1, dice2


dice = Dice()
print(dice.roll())
