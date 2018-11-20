import itertools
class Card:
    value_map = {0:0, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10,
                 'J':10, 'Q':10, 'K':10, 'A':(1,11)}
    suit_list = ['S', 'C', 'D', 'H', None]

    def __init__(self, value, suit):
        assert value in self.value_map.keys()
        assert suit in self.suit_list
        self.value = value
        self.suit = suit

    def __repr__(self):
        return str(self.value) + ' of ' + str(self.suit)

    def __gt__(self, other):
        val = self.get_value()
        if isinstance(other, Card):
            otherval = other.get_value()
            if isinstance(otherval, tuple):
                otherval = otherval[0]
        elif isinstance(other, int):
            otherval = other
        else:
            otherval = None
        if type(val) == tuple:
            if (val[0] > otherval) | (val[1] > otherval):
                return True
            else:
                return False
        else:
            return val > otherval

    def __lt__(self, other):
        val = self.get_value()
        if isinstance(other, Card):
            otherval = other.get_value()
            if isinstance(otherval, tuple):
                otherval = otherval[1]
        elif isinstance(other, int):
            otherval = other
        else:
            otherval = None
        if type(val) == tuple:
            if (val[0] < otherval) | (val[1] < otherval):
                return True
            else:
                return False
        else:
            return val < otherval

    def __le__(self, other):
        val = self.get_value()
        if isinstance(other, Card):
            otherval = other.get_value()
            if isinstance(otherval, tuple):
                otherval = otherval[1]
        elif isinstance(other, int):
            otherval = other
        else:
            otherval = None
        if type(val) == tuple:
            if (val[0] <= otherval) | (val[1] <= otherval):
                return True
            else:
                return False
        else:
            return val <= otherval

    def __ge__(self, other):
        val = self.get_value()
        if isinstance(other, Card):
            otherval = other.get_value()
            if isinstance(otherval, tuple):
                otherval = otherval[0]
        elif isinstance(other, int):
            otherval = other
        else:
            otherval = None
        if type(val) == tuple:
            if (val[0] >= otherval) | (val[1] >= otherval):
                return True
            else:
                return False
        else:
            return val >= otherval

    def __eq__(self, other):
        val = self.get_value()
        if isinstance(other, Card):
            otherval = other.get_value()
            if isinstance(otherval, tuple):
                otherval = otherval[0]
        elif isinstance(other, int):
            otherval = other
        else:
            otherval = None
        if type(val) == tuple:
            if (val[0] == otherval) | (val[1] == otherval):
                return True
            else:
                return False
        else:
            return val == otherval

    def __add__(self, other):
        val = self.get_value()
        if isinstance(other, Card):
            otherval = other.get_value()
            if isinstance(val, tuple) and isinstance(otherval, tuple):
                return tuple(i+j for i, j in itertools.product(val, otherval))
            elif isinstance(val, tuple) and isinstance(otherval, int):
                return tuple(i + otherval for i in val)
            elif isinstance(val, int) and isinstance(otherval, tuple):
                return tuple(i + val for i in otherval)
            else:
                return val + otherval
        else:
            raise ValueError

    def __sub__(self, other):
        val = self.get_value()
        if isinstance(other, Card):
            otherval = other.get_value()
            if isinstance(val, tuple) and isinstance(otherval, tuple):
                return tuple(i-j for i, j in itertools.product(val, otherval))
            elif isinstance(val, tuple) and isinstance(otherval, int):
                return tuple(i - otherval for i in val)
            elif isinstance(val, int) and isinstance(otherval, tuple):
                return tuple(val-i for i in otherval)
            else:
                return val - otherval
        else:
            raise ValueError

    def get_value(self):
        val = self.value_map[self.value]
        return val

    def is_even(self):
        val = self.get_value()
        if type(val) == tuple:
            return False
        else:
            return val % 2 == 0

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
        for a in range(2, val):
            if val % a == 0:
                return False
        return True

    def is_suit(self, suit):
        if self.suit == suit:
            return True
        else:
            return False



