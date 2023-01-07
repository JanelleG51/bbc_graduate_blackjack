from src.card import *

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def deal_card(self, card):
        self.cards.append(card)
        self.value += values[card.face]
        
        if card.face == 'Ace':
            self.aces += 1

    def aces_high_low(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

            
