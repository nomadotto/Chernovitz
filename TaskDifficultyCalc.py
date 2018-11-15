import inspect
import functools
import math
from Card import Card
from Deck import Deck
import random


class Task:
    def __init__(self, ncards, hand_size, task_hand=None):
        self.ncards = ncards
        self.hand_size = hand_size
        self.task_hand = task_hand
        self.component_cards = []
        self.requirements = []

    def __repr__(self):
        hand_size = str(self.hand_size)
        ncards = str(self.ncards)
        if self.task_hand is not None:
            task_hand = str(self.task_hand)
        else:
            task_hand = 'No'

        if len(self.component_cards) != 0:
            component_cards = sum(self.component_cards)
        else:
            component_cards = 'No'

        if len(self.requirements) != 0:
            requirements = sum(self.requirements)
        else:
            requirements = 'no'

        final_string = "A %s-sized Task requiring %s Cards with: %s Task Hand, %s Assembled " \
                       "Components and %s Requirements" % (hand_size, ncards, task_hand, component_cards, requirements)
        return final_string

    def make_task_hand(self, deck):
        try:
            cards = deck.draw(self.hand_size)
            self.task_hand = Deck(cards=cards)
        except IndexError:
            print ("Empty Deck")

    def make_component(self):
        component_cards = random.sample(self.task_hand, self.ncards)
        self.component_cards = Deck(cards=component_cards)

    def make_random_requirements(self):
        sr = self.make_random_suit_requirement()
        nr = self.make_random_number_requirement()
        self.requirements = [sr, nr]

    def set_requirements(self, requirements):
        self.requirements = requirements

    def check_component(self):
        comp_ok = True
        for req in self.requirements:
            comp_ok = comp_ok & (req(self.component_cards))
        return comp_ok

    def make_random_suit_requirement(self, nsuits=None):
        if nsuits is None:
            nsuits = random.randint(1, 4)
        req = Suit_Requirement(None)
        req.make_random_suit_requirement(self.ncards, nsuits)
        return req

    def make_random_number_requirement(self):
        number = random.randint(0, self.ncards*10)
        req = Number_Requirement(None)
        req.make_random_number_requirement(number)
        return req


class TaskChecker:
    def __init__(self):
        requirements_list = {'all_odd': self.all_odd, 'all_even': self.all_even, 'all_prime': self.all_prime,
                             'all_gt': self.all_gt, 'sum_eq': self.sum_eq, 'none_prime': self.none_prime,
                             'all_lt': self.all_lt, 'sum_gt': self.sum_gt, 'sum_lt': self.sum_lt, 'suits': self.is_suit}

    @staticmethod
    def all_odd(deck):
        for card in deck:
            if not card.is_odd():
                return False
        return True

    @staticmethod
    def all_even(deck):
        for card in deck:
            if not card.is_even():
                return False
        return True

    @staticmethod
    def all_prime(deck):
        for card in deck:
            if not card.is_prime():
                return False
        return True

    @staticmethod
    def all_gt(deck, value):
        for card in deck:
            if not card > value:
                return False
        return True

    @staticmethod
    def all_lt(deck, value):
        for card in deck:
            if not card < value:
                return False
        return True

    @staticmethod
    def none_prime(deck):
        for card in deck:
            if card.is_prime():
                return False
        return True

    @staticmethod
    def is_suit(card, suits):
        return card.suit in suits

    @staticmethod
    def is_suit_set(deck, suits_set):
        base = True
        if len(deck) != len(suits_set):
            return False
        else:
            for i in range(len(deck)):
                card = deck[i]
                suits = suits_set[i]
                base = base & TaskChecker.is_suit(card, suits)
        return base

    @staticmethod
    def sum_eq(deck, value):
        if sum(deck) == value:
            return True
        else:
            return False

    @staticmethod
    def sum_gt(deck, value):
        if sum(deck) > value:
            return True
        else:
            return False

    @staticmethod
    def sum_lt(deck, value):
        if sum(deck) < value:
            return True
        else:
            return False


class Suit_Requirement(TaskChecker):
    suit_list = ['S', 'C', 'D', 'H']

    def __init__(self, suits_set):
        TaskChecker.__init__(self)
        self.suits_set = suits_set

    def __repr__(self):
        return str(self.suits_set)

    def __add__(self, other):
        if isinstance(other, Number_Requirement):
            return str(other) + " and " + str(self)

    def check_suits(self, deck):
        return self.is_suit_set(deck, self.suits_set)

    def make_random_suit_requirement(self, ncards, nsuits):
        suits_list = []
        for i in range(ncards):
            suits = random.sample(self.suit_list, nsuits)
            suits_list.append(suits)
        return suits_list


class Number_Requirement(TaskChecker):

    def __init__(self, number_requirement, value=None):
        self.requirements_list = {'all_odd': self.all_odd, 'all_even': self.all_even, 'all_prime': self.all_prime,
                                  'all_gt': self.all_gt, 'sum_eq': self.sum_eq, 'none_prime': self.none_prime,
                                  'all_lt': self.all_lt, 'sum_gt': self.sum_gt, 'sum_lt': self.sum_lt}

        TaskChecker.__init__(self)
        self.req_name = number_requirement
        self.value = value
        self.number_requirement = self.requirements_list[number_requirement]

    def __repr__(self):
        if self.value is not None:
            return self.req_name + " with value " + str(self.value)
        else:
            return self.req_name

    def check_value(self, deck):
        return self.number_requirement(deck)

    def __add__(self, other):
        if isinstance(other, Suit_Requirement):
            return str(self) + " and " + str(other)
        else:
            raise ValueError

    def make_random_number_requirement(self, number):
        self.value = number
        self.req_name = random.choice(self.requirements_list.keys())
        self.number_requirement = self.requirements_list[self.req_name]
        if 'value' in inspect.getargspec(self.number_requirement).args:
            self.number_requirement = functools.partial(self.number_requirement, value=self.value)

