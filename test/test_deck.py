import unittest
from src.deck import Deck
from src.hand import Hand
from src.card import *
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
        self.hand.deal_card(self.deck.deal())
        self.assertTrue(self.hand.deal_card, 1)

    def test_validity_of_hand(self):
        """ Is the value of the added cards correct to ensure the hand is valid or invalid? """
        self.hand.deal_card(Card("Spades", "Two"))
        self.hand.deal_card(Card("Hearts", "Five"))
        self.assertEqual(self.hand.value, 7)
        """ Does the value of the hand update when a new card is introduced?"""
        self.hand.deal_card(Card("Clubs", "Eight"))
        self.assertEqual(self.hand.value, 15)

    def test_for_score_of_21_with_king_and_ace(self):
        """ Does the Ace remain at 11 when dealt with a card value of 10?"""
        self.hand.deal_card(Card("Hearts", "King"))
        self.hand.deal_card(Card("Diamonds", "Ace"))
        self.assertEqual(self.hand.value, 21)

    def test_for_score_of_21_with_king_queen_ace(self):
        """ Does the Ace adjust to a 1 when dealt with two cards with a value of 20? """
        self.hand.deal_card(Card("Hearts", "King"))
        self.hand.deal_card(Card("Diamonds", "Ace"))
        self.hand.deal_card(Card("Spades", "Queen"))
        self.hand.aces_high_low()
        self.assertEqual(self.hand.value, 21)

    def test_two_aces_and_nine_score_21(self):
        """ Does one Ace adjust to 1 when two aces and a nine are in hand? """
        self.hand.deal_card(Card("Spades", "Nine"))
        self.hand.deal_card(Card("Diamonds", "Ace"))
        self.hand.deal_card(Card("Hearts", "Ace"))
        self.hand.aces_high_low()
        self.assertEqual(self.hand.value, 21)


if __name__ == '__main__':
    unittest.main()
