from src.card import *

class Deck:
    """
    Creates a deck of cards from the imported Card class and variables.
    The deck class starts with an empty card array then loops through
    the fours suits and fourteen cards in the face and suits variables adding them to the empty array when instantiated. 
    This totals a number of 52 cards and does not take card value into 
    account - unit test passes.  
    """
    def __init__(self):
        self.cards = []
        for suit in suits:
            for face in faces:
                self.cards.append(Card(suit,face))
