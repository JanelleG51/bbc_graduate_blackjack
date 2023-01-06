import random
from src.deck import Deck
from src.card import *
from src.hand import Hand
from src.game_functions import *


def play():
    print('Welcome to BlackJack!')  
    
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.deal_card(deck.deal())
    player_hand.deal_card(deck.deal())

    show_hand(player_hand)


if __name__ == '__main__':
    play()
