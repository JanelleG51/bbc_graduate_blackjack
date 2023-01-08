# Blackjack Python Terminal Game  
## BBC Graduate Software Engineer Technical Assessment 
### Sep 2023 Admission Date 

This is a Python terminal BlackJack game built as part of the technical assessment for consideration to the position of Graduate Software Engineer Scheme with the BBC.

## Assumptions 

- This is a single player terminal game that deals only one hand.
- The aim of the player is to get a hand of 21.
- If the player achieves 21, the player wins and the game ends.
- If the player stands, the game ends.
- If the player scores over 21, the player is bust and the game ends.
- Aces score 1 or 11 depending on the value of the hand, the default score for aces is 11. If there is an ace in the hand and the total hand value exceeds 21, the ace is adjusted to score 1.

As the developer has taken a class-based, object oriented approach scalability is possible - additional decks and players can be added.

## Run and Test 
- To run this game, fork or clone the existing repository and run `python3 blackjack.py` in the terminal.
- To run the unit test, type `python3 -m unittest discover test` in the terminal - all available test cases will run

## Scenarios to be met / User Stories

Scenario | Expected Behaviour | Actual Behaviour | Manual Test Pass |
------- | ----------| ---------------------------- | ---------------------------|
 | Given I play a game of blackjack. When I am dealt my opening hand then I have two cards |When game is run using `python3 blackjack.py`, two cards of different values display in the terminal.| When `python3 blackjack.py` is run a welcome message displays in the terminal and the player is presented with two cards and their total value. The option to hit or stand is presented.| Yes
 | Given I have a valid hand of cards, when I choose to ‘hit’ then I receive another card and my score is updated | When the player opts to 'hit' one card is added to the existing hand and the value is updated in the terminal. If the player's hand value remains under 21, the player is again provided with the option to 'hit' or 'stand'.| On entering h and pressing enter, the player's hand is dealt a new card and to new total value is calculated and presented. If the total value remains under 21, the option to 'hit' or 'stand' is then displayed. | Yes
 | Given I have a valid hand of cards, when I choose to ‘stand’ then I receive no further cards and my score is evaluated | When the player is provided with the option to 'hit' or 'stand' and chooses to stand, their current hand and value remains unchanged. | When the player has a hand of less than 21 and they chose to 'stand' their hand and value remain unchanged. The game play does **not** break at this point but the hand and score do not change. | Yes
 | Given my score is updated or evaluated when it is 21 or less then I have a valid hand | When the players hand remains under 21 the option to 'hit' or 'stand' remains as an option to the player, when the player has a score of 21 they are informed they have BlackJack and the game ends. When the player's hand exceeds 21, they informed that they are 'bust' and the game ends.| When the player's score is under 21 they can 'hit' or 'stand'. Scores of 21 lead to the player being informed in the terminal they have BlackJack, scores over 21 inform the player they are bust and the game ends. | Yes
 | Given my score is updated when it is 22 or more then I am ‘bust’ and do not have a valid hand | Scores of 22 or more lead the player being 'bust' and no longer having a valid hand.| When the player's hand value exceeds 21 they are informed of their score and cards in the terminal and that they are 'bust' and game play ends.| Yes
 | Given I have a king and an ace, when my score is evaluated then my score is 21 | When the player's hand presents a King and an Ace of any suit, the player is informed they have BlackJack and the game ends. | When the game is run in the terminal and a King and Ace of any suit is presented, the player is informed thay have BlackJack.| Yes. Also confirmed in unittest.
 | Given I have a king, a queen, and an ace, when my score is evaluated then my score is 21 | When the player's hand presents a King, a Queen and an Ace of any suit, the player is informed they have BlackJack and the game ends.| When the game is run in the terminal and a King, a Queen and an Ace of any suit is presented, the player is informed thay have BlackJack.| Yes. Also confirmed in unittest.
 | Given that I have a nine, an ace, and another ace, when my score is evaluated then my score is 21 | When the player's hand presents two aces and a nine of any suit, the player is informed they have BlackJack and the game ends.|When the game is run in the terminal and two aces and a nine of any suit are presented, the player is informed thay have BlackJack.| Yes. Also confirmed in unittest.


 # Testing 
 ## Unit Testing 

 
Test Case| Failing Condition | Passing Condition | Pass |
------- | ----------| ---------------------------- | ---------------------------|
 | TC1: Create a deck of cards with 52 card | Run test without cards and incorrect number of cards | Create Card class and import to Deck class to loop through cards to return 52 cards | Yes
 | TC2: When the game starts, the player is dealt two cards | Run test with only one card in the player_hand while asserting the total lenght should be two. | Deal another card to the player_hand and run test again. | Yes
 | TC3: When a player ‘hits’ then they receive another card and their score is updated |   | The developer has tested that on hit one card is dealt using assertTrue but questions the validity of the test. | Yes but the developer feels it may need further work.
 | TC4: When a player ‘stands’ they receive no further cards and their score is evaluated | The developer was unable to run this test|| No
 | TC5:When a players score is 21 or less then they have a valid hand if they are over 21 they do not have a valid hand. | A player's hand is only valid if the values are correct. Adjust value of cards in card.py to reflect incorrect values i.e. change value of "two" to 5 and run test.  | Assess validity by adding correct card values to ensure calculations are correct and correctly updated when introducing a new card. | Yes
 | TC6: If a player has a king and an ace, then they score 21 | Set assertequal hand value to 21 and deal two cards that represent a score greater or lesser than 21. | Deal a King and and Ace and run test again.  | Yes
 |TC7: If a player has a king, a queen, and an ace, then they score 21 | Set assertequal hand value to 21 and deal a king, a queen and an ace.| Include aces_high_low function to adjust aces value and run test again.| Yes
 | TC8: If a player has a nine, an ace, and another ace, then they score 21 | Set assertequal hand value to 21 and deal two aces and a nine.| Include aces_high_low function to adjust aces value and run test again | Yes

## Environment

The developer used **VS Code** as the IDE and created a virtual environment. The below assumes that you have both VS Code and Git installed.

- Install Python
- Open a workspace and create python file   
- Create a virtual environment   
- `python -m venv <env name>`
- `<env name>/Scripts/Activate.bat`
- Go to `Command palette` – select python interpreter – if it doesn’t show, go to folder, scripts then select python. 


 


