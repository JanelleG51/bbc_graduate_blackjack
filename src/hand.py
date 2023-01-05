from src.card import *

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0

    def deal_card(self, card):
        self.cards.append(card)
        self.value +=values[card.face]


