import random
from src.card import *

class Deck:
    """
    Creates a deck of cards from the imported Card class and variables.
    The deck class starts with an empty card array then loops through
    the fours suits and fourteen cards in the face and suits variables. This builds Card objects and adds them to the empty array when instantiated. 
    This totals a number of 52 cards and does not take card value into 
    account - unit test passes.  
    """
    def __init__(self):
        self.cards = []
        for suit in suits:
            for face in faces:
                self.cards.append(Card(suit,face))

    def __str__(self):
        deck_build = ''
        for card in self.deck:
            deck_build += '\n'+card.__str__() 
        return 'The deck has:' + deck_build

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        deal_one_card = self.deck.pop()
        return deal_one_card

    

