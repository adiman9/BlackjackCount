# BlackjackCount

This program plays blackjack against itself using "perfect" chart based blackjack strategy. It takes the side of the dealer and the player and then plays a user specified number of hands. The game is played with 6 decks of cards that get shuffled into a virtual "shoe" then reshuffled at the end of the shoe, just like in a real casino.

The "player" playing against the dealer starts out with a user specified amount of money and bets the same amount every hand. After the total number of hands have been played, the amount of money each "player" has left is known. 

This allows the simulation of a huge amount of blackjack hands, using "perfect" strategy. This leads to an accurate representation of the house edge within the game of blackjack.

##Why

It was a nice coding challenge to try build an all emcompassing model to play both sides of the game "perfectly". It is also nice to be able to have hard data to show the house edge over a huge sample of hands, something that isnt possible in real life due to temporal and fiscal limitations.

##Other Features.
The code also tracks the "count" of the deck for every hand and stores it in an array along with the amount won and lost in every hand. This allows a cross referencing of the count of the deck at any given point in time with the amount the player is winning. This will build up a quantative correlation between profitability and the count of the deck.

##TODO
- allow custom user defined betting strategies
