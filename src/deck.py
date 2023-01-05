import random
from src.card import *

class Deck:
    """
    Creates a deck of cards from the imported Card class and variables.
    The deck class starts with an empty card list then loops through
    the fours suits and fourteen cards in the face and suits variables. This builds Card objects and adds them to the empty list when instantiated. 
    This totals a number of 52 cards and does not take card value into account - unit test passes.  
    """
    def __init__(self):
        self.cards = []
        for suit in suits:
            for face in faces:
                self.cards.append(Card(suit,face))

    def __str__(self):
        """
        Provides the print string for each card.
        """
        deck_build = ''
        for card in self.deck:
            deck_build += '\n'+card.__str__() 
        return 'The deck has:' + deck_build

    def shuffle(self):
        """
        Shuffles the deck of 52 cards using the built in random function.
        """
        random.shuffle(self.cards)

    def deal(self):
        """
        When the deal function is called, one card is removed from the deck using the pop function ready to be added to the empty cards list stored in the Hand class.
        """
        deal_one_card = self.cards.pop()
        return deal_one_card

    

