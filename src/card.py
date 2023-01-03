class Card:
    def __init__(self, suit, face):
        self.suit = suit
        self.face = face
    
    def __str__(self):
        return self.face + ' of ' + self.suit

