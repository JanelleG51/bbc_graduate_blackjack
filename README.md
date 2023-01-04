# Blackjack Python Terminal Game  
## BBC Graduate Software Engineer Technical Assessment 
### Sep 2023 Admission Date 

This is a Python terminal BlackJack game built as part of the technical assessment for consideration to the position of Graduate Software Engineer for the BBC.

## Scenarios to be met / User Stories

Scenario | Expected Behaviour | Actual Behaviour | Pass |
------- | ----------| ---------------------------- | ---------------------------|
 | Given I play a game of blackjack. When I am dealt my opening hand then I have two cards |||
 | Given I have a valid hand of cards, when I choose to ‘hit’ then I receive another card and my score is updated |||
 | Given I have a valid hand of cards, when I choose to ‘stand’ then I receive no further cards and my score is evaluated |||
 | Given my score is updated or evaluated when it is 21 or less then I have a valid hand |||
 | Given my score is updated when it is 22 or more then I am ‘bust’ and do not have a valid hand |||
 | Given I have a king and an ace, when my score is evaluated then my score is 21 |||
 | Given I have a king, a queen, and an ace, when my score is evaluated then my score is 21 |||
 | Given that I have a nine, an ace, and another ace, when my score is evaluated then my score is 21 |||


 # Testing 
 ## Unit Testing 

 
Test Case| Failing Condition | Passing Condition | Pass |
------- | ----------| ---------------------------- | ---------------------------|
 | TC1: Create a deck of cards with 52 card | Run test without cards | Create Card class and import to Deck class to loop through cards | Yes
 | TC2: When a player ‘hits’ then they receive another card and their score is updated |||
 | TC3: When a player ‘stands’ they receive no further cards and their score is evaluated |||
 | TC4:When a players score is 21 or less then they have a valid hand |||
 | TC5: When a players hand is 22 or more then they are ‘bust’ and do not have a valid hand |||
 | TC6: If a player has a king and an ace, then they score 21 |||
 |TC7: If a player has a king, a queen, and an ace, then they score 21 |||
 | TC8: If a player has a nine, an ace, and another ace, then they score 21 |||


 ## Assumptions 

 ## Environment

 IDE VSCode 
- Install Python and create a Python file  
- Virtual environment   
- Python -m venv Env name
- Env name/Scripts/Activate.bat
- Command palette – select python interpreter – if it doesn’t show, go to folder, scripts then select python 


 


