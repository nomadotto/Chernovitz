
from Card import Card


class Deck:
    def __init__(self, cards=None):
        if cards:
            self.cards = cards
        else:
            self.cards = []

        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= len(self.cards):
            raise StopIteration
        else:
            self.current += 1
            return self.cards[self.current - 1]

    def add_card(self, card):
        self.cards.append(card)

    def make_default_deck(self):
        for value in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']:
            for suit in ['S', 'C', 'D', 'H']:
                self.add_card(Card(value=value, suit=suit))
                self.add_card(Card(value=value, suit=suit))
