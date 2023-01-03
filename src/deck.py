from src.card import Card

class Deck:
    def __init__(self):
        self.cards = []
        for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for face in range (1, 14):
                self.cards.append(Card(suit,face))
