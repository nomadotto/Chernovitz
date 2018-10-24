
class Card:
    value_map = {1:1,2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10,
                 'J':10, 'Q':10, 'K':10, 'A':(1,11)}
    suit_list = ['S', 'C', 'D', 'H']

    def __init__(self, value, suit):
        assert value in self.value_map.keys()
        assert suit in self.suit_list
        self.value = value
        self.suit = suit

    def __gt__(self, other):
        val = self.get_value()
        if type(val) == tuple:
            if (val[0] > other) | (val[1] > other):
                return True
            else:
                return False
        else:
            return val > other

    def __lt__(self, other):
        val = self.get_value()
        if type(val) == tuple:
            if (val[0] < other) | (val[1] < other):
                return True
            else:
                return False
        else:
            return val < other

    def __le__(self, other):
        val = self.get_value()
        if type(val) == tuple:
            if (val[0] <= other) | (val[1] <= other):
                return True
            else:
                return False
        else:
            return val <= other

    def __ge__(self, other):
        val = self.get_value()
        if type(val) == tuple:
            if (val[0] >= other) | (val[1] >= other):
                return True
            else:
                return False
        else:
            return val >= other

    def __eq__(self, other):
        val = self.get_value()
        if type(val) == tuple:
            if (val[0] == other) | (val[1] == other):
                return True
            else:
                return False
        else:
            return val == other

    def __add__(self, other):
        val = self.get_value()
        if type(val) == tuple:
            return val[0] + other, val[1] +other
        else:
            return val + other

    def __sub__(self, other):
        val = self.get_value()
        if type(val) == tuple:
            return val[0] + other, val[1] +other
        else:
            return val + other

    def get_value(self):
        val = self.value_map[self.value]
        return val

    def is_even(self):
        val = self.get_value()
        if type(val) == tuple:
            return False
        else:
            return val % 2 ==0

    def is_odd(self):
        val = self.get_value()
        if type(val) == tuple:
            return True
        else:
            return val % 2 == 1

    def is_prime(self):
        val = self.get_value()
        if type(val) == tuple:
            return True
        for a in range(a, val):
            if a % val == 0:
                return False
        return True

    def is_suit(self, suit):
        if self.suit == suit:
            return True
        else:
            return False



