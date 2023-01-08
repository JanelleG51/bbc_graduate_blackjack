# Blackjack Python Terminal Game  
## BBC Graduate Software Engineer Technical Assessment 
### Sep 2023 Admission Date 

This is a Python terminal BlackJack game built as part of the technical assessment for consideration to the position of Graduate Software Engineer Scheme with the BBC.

## Scenarios to be met / User Stories

Scenario | Expected Behaviour | Actual Behaviour | Manual Test Pass |
------- | ----------| ---------------------------- | ---------------------------|
 | Given I play a game of blackjack. When I am dealt my opening hand then I have two cards |When game is run using `python3 blackjack.py`, two cards of different values display in the terminal.| When `python3 blackjack.py` is run a welcome message displays in the terminal and the player is presented with two cards and their total value. The option to hit or stand is presented.| Yes
 | Given I have a valid hand of cards, when I choose to ‘hit’ then I receive another card and my score is updated | When the player opts to 'hit' one card is added to the existing hand and the value is updated in the terminal. If the player's hand value remains under 21, the player is again provided with the option to 'hit' or 'stand'.| On entering h and pressing enter, the player's hand is dealt a new card and to new total value is calculated and presented. If the total value remains under 21, the option to 'hit' or 'stand' is then displayed. | Yes
 | Given I have a valid hand of cards, when I choose to ‘stand’ then I receive no further cards and my score is evaluated | When the player is provided with the option to 'hit' or 'stand' and chooses to stand, their current hand and value remains unchanged. | When the player has a hand of less than 21 and they chose to 'stand' their hand and value remain unchanged.| Yes
 | Given my score is updated or evaluated when it is 21 or less then I have a valid hand | When the players hand remains under 21 the option to 'hit' or 'stand' remains as an option to the player, when the player has a score of 21 they are informed they have BlackJack and the game ends. When the player's hand exceeds 21, they informed that they are 'bust' and the game ends.| When the player's score is under 21 they can 'hit' or 'stand'. Scores of 21 lead to the player being informed in the terminal they have BlackJack, scores over 21 inform the player they are bust and the game ends. | Yes
 | Given my score is updated when it is 22 or more then I am ‘bust’ and do not have a valid hand | Scores of 22 or more lead the player being 'bust' and no longer having a valid hand.| When the player's hand value exceeds 21 they are informed of their score and cards in the terminal and that they are 'bust' and game play ends.| Yes
 | Given I have a king and an ace, when my score is evaluated then my score is 21 |||
 | Given I have a king, a queen, and an ace, when my score is evaluated then my score is 21 |||
 | Given that I have a nine, an ace, and another ace, when my score is evaluated then my score is 21 |||


 # Testing 
 ## Unit Testing 

 
Test Case| Failing Condition | Passing Condition | Pass |
------- | ----------| ---------------------------- | ---------------------------|
 | TC1: Create a deck of cards with 52 card | Run test without cards | Create Card class and import to Deck class to loop through cards | Yes
 | TC2: When the game starts, the player is dealt two cards | | |
 | TC3: When a player ‘hits’ then they receive another card and their score is updated |||
 | TC4: When a player ‘stands’ they receive no further cards and their score is evaluated |||
 | TC5:When a players score is 21 or less then they have a valid hand |||
 | TC6: When a players hand is 22 or more then they are ‘bust’ and do not have a valid hand |||
 | TC7: If a player has a king and an ace, then they score 21 |||
 |TC8: If a player has a king, a queen, and an ace, then they score 21 |||
 | TC9: If a player has a nine, an ace, and another ace, then they score 21 |||


 ## Assumptions 

 ## Environment

 IDE VSCode 
- Install Python and create a Python file  
- Virtual environment   
- Python -m venv Env name
- Env name/Scripts/Activate.bat
- Command palette – select python interpreter – if it doesn’t show, go to folder, scripts then select python 


 


