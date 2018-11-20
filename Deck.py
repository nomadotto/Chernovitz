import itertools
from Card import Card
import random
import collections

class Deck:
    def __init__(self, cards=None):
        if cards:
            self.cards = cards
        else:
            self.cards = []

        self.current = 0

    def __iter__(self):
        return self

    def __repr__(self):
        return "A deck of " + str(len(self.cards))

    def __getitem__(self, item):
        return self.cards[item]

    def __len__(self):
        return len(self.cards)

    def __eq__(self, other):
        total = self.sum()
        if isinstance(other, int):
            if isinstance(total, int):
                if total == other:
                    return True
                else:
                    return False
            elif isinstance(total, tuple):
                if True in [i == other for i in total]:
                    return True
                else:
                    return False
            else:
                return False
        if isinstance(other, Deck):
            return collections.Counter(self.cards) == collections.Counter(other.cards)

    def __gt__(self, other):
        total = self.sum()
        if isinstance(other, int):
            if isinstance(total, int):
                if total > other:
                    return True
                else:
                    return False
            elif isinstance(total, tuple):
                if True in [i >other for i in total]:
                    return True
                else:
                    return False
            else:
                return False
        elif isinstance(other, Deck):
            otherval = other.sum()
            if isinstance(otherval, tuple) & isinstance(total, tuple):
                return max(total) > max(otherval)
            elif isinstance(otherval, tuple) & isinstance(total, int):
                return total > max(otherval)
            elif isinstance(otherval, int) & isinstance(total, tuple):
                return max(total) > otherval
            else:
                return total > otherval

        else:
            return ValueError

    def __lt__(self, other):
        total = self.sum()
        if isinstance(other, int):
            if isinstance(total, int):
                if total < other:
                    return True
                else:
                    return False
            elif isinstance(total, tuple):
                if True in [i < other for i in total]:
                    return True
                else:
                    return False
            else:
                return False
        elif isinstance(other, Deck):
            otherval = other.sum()
            if isinstance(otherval, tuple) & isinstance(total, tuple):
                return max(total) < max(otherval)
            elif isinstance(otherval, tuple) & isinstance(total, int):
                return total < max(otherval)
            elif isinstance(otherval, int) & isinstance(total, tuple):
                return max(total) < otherval
            else:
                return total < otherval

        else:
            return ValueError

    def next(self):
        if self.current >= len(self.cards):
            self.current = 0
            raise StopIteration
        else:
            self.current += 1
            return self.cards[self.current - 1]

    def add_card(self, card):
        self.cards.append(card)

    def make_default_deck(self):
        for value in [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']:
            for suit in ['S', 'C', 'D', 'H']:
                self.add_card(Card(value=value, suit=suit))
                self.add_card(Card(value=value, suit=suit))

    def sum(self):
        total = 0
        for card in self.cards:
            val = card.get_value()
            if isinstance(val, int) & isinstance(total, int):
                total += val
            elif isinstance(val, tuple) & isinstance(total, int):
                total = tuple(i + total for i in val)
            elif isinstance(val, int) & isinstance(total, tuple):
                total = tuple(i + val for i in total)
            elif isinstance(val, tuple) & isinstance(total, tuple):
                total = tuple(i+j for i, j in itertools.product(val, total))
        return total

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, ncards = 1):
        cards = []
        while len(cards) < ncards:
            cards.append(self.cards.pop())
        return cards

