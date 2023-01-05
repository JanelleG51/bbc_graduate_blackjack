import unittest
from src.deck import Deck
from src.hand import Hand


class DeckTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.deck = Deck()

    def tearDown(self):  # this method will be run after each tests
        pass

    # any method beginning with 'test' will be run by unittest
    def test_number_of_cards(self):
        number_of_cards = len(self.deck.cards)
        self.assertEqual(number_of_cards, 52)

    def test_player_dealt_two_cards(self):
        player_hand = Hand()
        player_hand.deal_card(self.deck.deal())
        player_hand.deal_card(self.deck.deal())
        self.assertEqual(len(player_hand.cards), 2)

    def test_hand_is_updated_on_hit(self):



if __name__ == '__main__':
    unittest.main()
