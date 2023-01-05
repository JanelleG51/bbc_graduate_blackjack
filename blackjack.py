import random
from src.deck import Deck
from src.card import *
from src.hand import Hand


def play():
    print('Welcome to BlackJack!')  
    
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.deal_card(deck.deal())
    player_hand.deal_card(deck.deal())


if __name__ == '__main__':
    play()
