import unittest
from src.deck import Deck
from src.hand import Hand
from src.game_functions import *


class DeckTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.deck = Deck()
        self.hand = Hand()

    def tearDown(self):  # this method will be run after each tests
        pass

    # any method beginning with 'test' will be run by unittest
    def test_number_of_cards(self):
        """ Does the deck have 52 cards? """
        number_of_cards = len(self.deck.cards)
        self.assertEqual(number_of_cards, 52)

    def test_player_dealt_two_cards(self):
        """ Is the player dealt two cards when the game starts? """
        player_hand = Hand()
        player_hand.deal_card(self.deck.deal())
        player_hand.deal_card(self.deck.deal())
        self.assertEqual(len(player_hand.cards), 2)

    def test_one_card_dealt_on_hit(self):
        """ Does the players hand update with one card on hit? """
        one_card_dealt_on_hit = hit(self.deck, self.hand)
        self.hand.deal_card(self.deck.deal())
        self.assertTrue(self.hand.deal_card, 1)



    



if __name__ == '__main__':
    unittest.main()
