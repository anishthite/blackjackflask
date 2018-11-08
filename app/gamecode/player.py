'''
Created on Jul 1, 2018

@author: anish
'''
class Player:

    def __init__(self, cash):
        self.cash = cash
        self.hand = []

    def show(self):
        show = []
        for card in self.hand:
            show.append(card.faceup())
        return show

    def count(self):
        total = 0
        for card in self.hand:
            total += card.derive_value()
        return total

class Dealer(Player):

    def __init__(self):
        self.hand = []

    def show(self):
        show = []
        show.append(self.hand[0].faceup())
        show.append(self.hand[1].facedown())
        return show

    def show_final(self):
        show = []
        for card in self.hand:
            show.append(card.faceup())
        return show