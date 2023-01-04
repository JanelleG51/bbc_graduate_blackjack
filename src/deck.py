from src.card import *

class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for face in faces:
                self.cards.append(Card(suit,face))
