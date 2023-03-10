class Card:
    """
    Provides a single instance of a card based on suit and face, and 
    is the basis for building the required deck of cards. 
    """
    def __init__(self, suit, face):
        self.suit = suit
        self.face = face
    
    def __str__(self):
        return self.face + ' of ' + self.suit

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
faces = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7,'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
          'Queen':10, 'King':10, 'Ace':11}
