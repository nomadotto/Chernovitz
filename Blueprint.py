from TaskDifficultyCalc import Task


class Blueprint:
    def __init__(self, nplayers, tasks=None, card_split=None):
        self.nplayers = nplayers
        if tasks is not None:
            try:
                assert nplayers == len(tasks)
                self.tasks = tasks
            except AssertionError:
                raise ValueError('Number of tasks and number of players do not agree')
        else:
            self.tasks = tasks

        if card_split is not None:
            try:
                assert nplayers == len(card_split)
                self.card_split = card_split
            except AssertionError:
                raise ValueError('Size of Cardsplit and number of players do not agree')

        else:
            self.card_split = card_split

    def make_random_tasks(self):
        tasks = []
        if self.card_split is None:
            self.make_card_split()
        for i in range(self.nplayers):
            cards = self.card_split[i]
            ncards = cards / 6
            t = Task(ncards=ncards, hand_size=cards)
            t.make_random_requirements()
            tasks.append(t)
        self.tasks = tasks

    def make_card_split(self, deck_size=104):
        cards = [0]*self.nplayers
        remaining_cards = deck_size - 5*self.nplayers - 6
        while remaining_cards > 3*self.nplayers:
                elem = map(lambda x: x+3, cards)
                cards = elem
                remaining_cards += -3*self.nplayers
        while remaining_cards > ((self.nplayers/2)*3):
            for i in range(self.nplayers/2 + 1, self.nplayers):
                cards[i] += 3
                remaining_cards += -3

        while remaining_cards > 0:
            for i in range(self.nplayers-1, 0, -1):
                cards[i] += 1
                remaining_cards += -1
        self.card_split = cards
