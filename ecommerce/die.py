import random


class Diece:

    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first,second # don't use paranthesis, to return tuple

die = Diece()

print(die.roll())
