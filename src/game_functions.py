# This file contains all non class-based game functions
playing = True

def show_hand(player):
    print("\nPlayer's hand:", *player.cards, sep='\n')
    print("Player's hand =", player.value)


def hit(deck, hand):
    """
    When a player 'hits', another card is popped from the deck, added to their hand and the value updated.
    """
    hand.deal_card(deck.deal())


def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")

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

