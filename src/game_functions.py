# This file contains all non class-based game functions

playing = True

def show_hand(player):
    """
    Displays the player's hand in the terminal as strings and shows the total value of the cards
    """
    print("\nPlayer's hand:", *player.cards, sep='\n')
    print("Player's hand =", player.value)


def hit(deck, hand):
    """
    When a player 'hits', one card is popped from the deck, added to their existing hand and the value updated. If the value of the card will take the hand over 21 and there is an ace in hand, the score will be adjusted to keep the player under 21.
    """
    hand.deal_card(deck.deal())
    hand.aces_high_low()


def hit_or_stand(deck, hand):
    global playing

    """
    While that game is playing and the player's hand remains under 21, they player will have the option to 'hit' until they win or bust, or stand.
    """

    while True:
        x = input("You're still under 21! Would you like to Hit or Stand? Enter 'h' or 's' ")

        if x[0].lower() == 'h':
            hit(deck, hand)
            show_hand(hand)

        elif x[0].lower() == 's':
            print("Player stands. Player's hand = ", hand.value)
            playing = False
        
        else:
            print("Sorry, please try again.")
            continue
        break


        