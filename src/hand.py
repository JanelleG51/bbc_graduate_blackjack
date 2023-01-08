from src.card import *

class Hand:
    def __init__(self):
        """
        Creates and empty list for the players hand, sets the value of the hand to 0 and the number of aces to 0. Aces will be counted as two values depending on the value of the hand and we need to know how many aces are in hand.
        """
        self.cards = []
        self.value = 0
        self.aces = 0

    def deal_card(self, card):
        """
        Appends a single instance of a card to the cards list and adds the value of all cards. If an ace is present, the number of aces in the hand are added to self.aces.
        """
        self.cards.append(card)
        self.value += values[card.face]
        
        if card.face == 'Ace':
            self.aces += 1

    def aces_high_low(self):
        """
        If the total value of the hand is over 21, aces are then scored as 1.
        """
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def hand_not_bust(self):
        if self.value > 21:
            return False  
        return True

            
