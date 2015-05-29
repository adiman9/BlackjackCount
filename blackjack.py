from random import randint


class Shoe(object):

    def __init__(self, numDecks):
        self.numDecks = numDecks
        self.shoe = [None] * numDecks * 52

        for x in range(0, numDecks):
            for y in range(0, 4):
                for z in range(1, 14):
                    if z > 10:
                        self.shoe[z-1+y*13+x*52] = 10
                    elif z == 1:
                        self.shoe[z-1+y*13+x*52] = 11
                    else:
                        self.shoe[z-1+y*13+x*52] = z

        self.shuffle()


    def shuffle(self):

        for i in range(1, 2):
            for j in range(0, len(self.shoe)):
                randomNum = int(round(randint(0, len(self.shoe)-1)))
                temp = self.shoe[j]
                self.shoe[j] = self.shoe[randomNum]
                self.shoe[randomNum] = temp

    def deal(self):
        return self.shoe.pop()


class Hand(object):

    hand = []
    newSplit = [None]
    double = "hello"

    def __init__(self, hand = []):
        if len(hand) is not 0:
            self.hand = hand
        else:
            self.hand = [None] * 2
            self.dealHand()

    def dealHand(self):
        self.hand[0] = shoe.deal()
        self.hand[1] = shoe.deal()

    def hit(self):
        self.hand.append(shoe.deal())

    def double(self):
        self.hand.append(shoe.deal())
        self.double = True

    def split(self):
        splitHand = [None]
        splitHand[0] = self.hand.pop()
        splitHand.append(shoe.deal())

        self.newSplit[0] = Hand(splitHand)

        self.hit()

    def isSoft(self):
        for x in self.hand:
            if x is 11:
                return True
        return False

    def softConvert(self):
        for x in range(len(self.hand)):
            if self.hand[x] is 11:
                self.hand[x] = 1

    def handValue(self):
        value = 0

        for x in self.hand:
            value = value + x

        return value

    def isBlackjack(self):

        if len(self.hand) is 2 and self.handValue() is 21:
            return True
        return False

    def isAPair(self):
        if len(self.hand) is 2 and self.hand[0] == self.hand[1]:
            return True
        return False

    def getDouble(self):
	if str(self.double) is "True":
	    return True
	return False 


class Player(object):
    
    def __init__(self, bankroll):
	self.bankroll = bankroll
	
def playerPlay(hand, dealer):
    stand = False
    notSplitting = False

    while not stand:

        if hand.handValue() > 21 and not hand.isSoft():
            stand = True
        elif hand.isAPair() and not notSplitting:
            if splitChart[hand.hand[0]-1][dealer.hand[0]-2] is 0:
                notSplitting = True
            else:
		print "split"
                hand.split()
                return hand.newSplit[0]
        elif hand.isSoft():
            if hand.handValue() > 21:
                hand.softConvert()
            elif softChart[hand.handValue()-1][dealer.hand[0]-2] is 1:
                hand.hit()
            elif softChart[hand.handValue()-1][dealer.hand[0]-2] is 0:
                stand = True
            elif softChart[hand.handValue()-1][dealer.hand[0]-2] is 2:
		if len(hand.hand) is 2:
                    hand.double()
		    if hand.handValue() > 21:
		        hand.softConvert()
                    stand = True
		else: 
		    hand.hit()
            else:
                stand = True

        else:
            if hardChart[hand.handValue()-1][dealer.hand[0]-2] is 1:
                hand.hit()
            elif hardChart[hand.handValue()-1][dealer.hand[0]-2] is 0:
                stand = True
            elif len(hand.hand) is 2 and hardChart[hand.handValue()-1][dealer.hand[0]-2] is 2:
                hand.double()
                stand = True
            else:
                stand = True

    return "cont"



def dealerPlay(hand):
    stand = False

    while not stand:
        if hand.handValue() < 17:
            hand.hit()
        elif hand.handValue() > 21:
            if hand.isSoft():
                hand.softConvert()
                hand.hit()
            else:
                stand = True
        else:
            stand = True

def decideWinner(player, dealer):
    if player.handValue() > 21:
        print "Player Bust, Dealer wins!"
	if str(player.getDouble()) is "True":
	    return -2
	return -1
    elif dealer.isBlackjack() and not player.isBlackjack():
        print "Dealer has Blackjack!"
	if str(player.getDouble()) is "True":
	    return -2
	return -1
    elif dealer.isBlackjack() and player.isBlackjack():
        print "Player and Dealer both have Blackjack!"
	return 0
    elif player.isBlackjack():
        print "Player has Blackjack!"
	return 1.5
    elif player.handValue() < 22 and dealer.handValue() > 21:
        print "dealer bust, player wins!"
	if str(player.getDouble()) is "True":
	    return 2
	return 1
    elif player.handValue() > dealer.handValue():
        print "player wins!"
	if str(player.getDouble()) is "True":
	    return 2
	return 1
    elif dealer.handValue() > player.handValue():
        print "dealer wins"
	if str(player.getDouble()) is "True":
	    return -2
	return -1
    else:
        print "its a tie!"
	return 0


def play(numPlayers, iterations, bankroll, betSize):

    playerRolls = [object]*numPlayers	
	
    for x in range(0, numPlayers):
	playerRolls[x] = Player(bankroll)	

    for j in range(0, iterations):
	players = []	

	for x in range(0, numPlayers):
	    players.append([])

	dealerHand = Hand()
	dealerPlay(dealerHand)
	
	for x in range(0, numPlayers):
	    players[x].append(Hand())
	
	complete = False

	for y in range(0, numPlayers):
	    complete = False
   	    x = 0

	    while not complete:
		if len(players[y]) > x:
		    splitHand = playerPlay(players[y][x], dealerHand)

		    if splitHand is "cont":
			x = x + 1
		    else:
			players[y].append(splitHand)				
		else:
		    for z in players[y]:
			win = decideWinner(z, dealerHand)
			playerRolls[y].bankroll = playerRolls[y].bankroll + win*betSize
		    complete = True

    for x in range(0, numPlayers):
	print len(players[x])
	for y in range(0, len(players[x])):
	    print players[x][y].hand
	    print players[x][y].handValue()
	print playerRolls[x].bankroll
	print "\n" 

softChart = [
                [   1, 1, 1, 1, 1, 1, 1, 1, 1, 1   ],
                [   1, 1, 1, 1, 1, 1, 1, 1, 1, 1   ],
                [   1, 1, 1, 1, 1, 1, 1, 1, 1, 1   ],
                [   1, 1, 1, 1, 1, 1, 1, 1, 1, 1   ],
                [   1, 1, 1, 1, 1, 1, 1, 1, 1, 1   ],
                [   1, 1, 1, 1, 1, 1, 1, 1, 1, 1   ],
                [   1, 1, 1, 1, 1, 1, 1, 1, 1, 1   ],
                [   1, 1, 1, 1, 1, 1, 1, 1, 1, 1   ],
                [   1, 1, 1, 1, 1, 1, 1, 1, 1, 1   ],
                [   1, 1, 1, 1, 1, 1, 1, 1, 1, 1   ],
                [   1, 1, 1, 1, 1, 1, 1, 1, 1, 1   ],
                [   1, 1, 1, 1, 1, 1, 1, 1, 1, 1   ],
                [   1, 1, 2, 2, 2, 1, 1, 1, 1, 1   ],
                [   1, 1, 2, 2, 2, 1, 1, 1, 1, 1   ],
                [   1, 1, 2, 2, 2, 1, 1, 1, 1, 1   ],
                [   1, 1, 2, 2, 2, 1, 1, 1, 1, 1   ],
                [   2, 2, 2, 2, 2, 1, 1, 1, 1, 1   ],
                [   0, 2, 2, 2, 2, 0, 0, 1, 1, 0   ],
                [   0, 0, 0, 0, 0, 0, 0, 0, 0, 0   ],
                [   0, 0, 0, 0, 0, 0, 0, 0, 0, 0   ],
                [   0, 0, 0, 0, 0, 0, 0, 0, 0, 0   ]
            ]

splitChart = [
                [   0, 0, 0, 0, 0, 0, 0, 0, 0, 0   ],
                [   0, 0, 0, 0, 0, 0, 0, 0, 0, 0   ],
                [   1, 1, 1, 1, 1, 1, 0, 0, 0, 0   ],
                [   1, 1, 1, 1, 1, 1, 0, 0, 0, 0   ],
                [   0, 0, 0, 1, 0, 0, 0, 0, 0, 0   ],
                [   0, 0, 0, 0, 0, 0, 0, 0, 0, 0   ],
                [   1, 1, 1, 1, 1, 1, 0, 0, 0, 0   ],
                [   1, 1, 1, 1, 1, 1, 1, 0, 0, 0   ],
                [   1, 1, 1, 1, 1, 0, 1, 1, 0, 0   ],
                [   0, 0, 0, 0, 0, 0, 0, 0, 0, 0   ],
                [   1, 1, 1, 1, 1, 1, 1, 1, 1, 1   ]
            ]

hardChart = [
                [   1, 1, 1, 1, 1, 1, 1, 1, 1, 1    ],
                [   1, 1, 1, 1, 1, 1, 1, 1, 1, 1    ],
                [   1, 1, 1, 1, 1, 1, 1, 1, 1, 1    ],
                [   1, 1, 1, 1, 1, 1, 1, 1, 1, 1    ],
                [   1, 1, 1, 1, 1, 1, 1, 1, 1, 1    ],
                [   1, 1, 1, 1, 1, 1, 1, 1, 1, 1    ],
                [   1, 1, 1, 1, 1, 1, 1, 1, 1, 1    ],
                [   1, 1, 1, 1, 1, 1, 1, 1, 1, 1    ],
                [   2, 2, 2, 2, 2, 1, 1, 1, 1, 1    ],
                [   2, 2, 2, 2, 2, 2, 2, 2, 1, 1    ],
                [   2, 2, 2, 2, 2, 2, 2, 2, 2, 2    ],
                [   1, 1, 0, 0, 0, 1, 1, 1, 1, 1    ],
                [   0, 0, 0, 0, 0, 1, 1, 1, 1, 1    ],
                [   0, 0, 0, 0, 0, 1, 1, 1, 1, 1    ],
                [   0, 0, 0, 0, 0, 1, 1, 1, 1, 1    ],
                [   0, 0, 0, 0, 0, 1, 1, 1, 1, 1    ],
                [   0, 0, 0, 0, 0, 0, 0, 0, 0, 0    ],
                [   0, 0, 0, 0, 0, 0, 0, 0, 0, 0    ],
                [   0, 0, 0, 0, 0, 0, 0, 0, 0, 0    ],
                [   0, 0, 0, 0, 0, 0, 0, 0, 0, 0    ],
                [   0, 0, 0, 0, 0, 0, 0, 0, 0, 0   ]
            ]


shoe = Shoe(6)

play(7, 10, 10000,  1)



#TODO
# look into passing to a split hand that it cannot acheive blackjack
# look into how to destroy objects to start a new hand
# look to reshuffle the cards when the shoe nears the end
