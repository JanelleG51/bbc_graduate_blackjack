import random
from src.deck import Deck
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

    while player_hand.value < 21:
        hit_or_stand(deck, player_hand)

    if player_hand.value > 21:
        print("Player busts!")
    
    if player_hand.value == 21:
        print("BlackJack! You win!!")
       

if __name__ == '__main__':
    play()
