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
    double = False

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

def playerPlay(hand, dealer):
    stand = False
    notSplitting = False

    while not stand:

        if hand.handValue() > 21 and not hand.isSoft():
            print "standing"
            stand = True
        elif hand.isAPair() and not notSplitting:
            if splitChart[hand.hand[0]-1][dealer.hand[0]-2] is 0:
                notSplitting = True
                print "pair not splitting"
            else:
                print "splitting..."
                hand.split()
                return hand.newSplit[0]
        elif hand.isSoft():
            if hand.handValue() > 21:
                print "soft converting"
                hand.softConvert()
            elif softChart[hand.handValue()-1][dealer.hand[0]-2] is 1:
                hand.hit()
                print "soft hitting"
            elif softChart[hand.handValue()-1][dealer.hand[0]-2] is 0:
                stand = True
                print "soft standing"
            elif softChart[hand.handValue()-1][dealer.hand[0]-2] is 2:
		if len(hand.hand) is 2:
                    print "soft double down"
                    hand.double()
		    hand.softConvert()
                    stand = True
		else: 
		    hand.hit()
            else:
                stand = True

        else:
            if hardChart[hand.handValue()-1][dealer.hand[0]-2] is 1:
                hand.hit()
                print "hard hit"
            elif hardChart[hand.handValue()-1][dealer.hand[0]-2] is 0:
                stand = True

                print "hard stand"
            elif len(hand.hand) is 2 and hardChart[hand.handValue()-1][dealer.hand[0]-2] is 2:
                hand.double()
                stand = True
                print "hard double"
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
    elif dealer.isBlackjack() and not player.isBlackjack():
        print "Dealer has Blackjack!"
    elif dealer.isBlackjack() and player.isBlackjack():
        print "Player and Dealer both have Blackjack!"
    elif player.isBlackjack():
        print "Player has Blackjack!"
    elif player.handValue() < 22 and dealer.handValue() > 21:
        print "dealer bust, player wins!"
    elif player.handValue() > dealer.handValue():
        print "player wins!"
    elif dealer.handValue() > player.handValue():
        print "dealer wins"
    else:
        print "its a tie!"


def play():

    dealerHand = Hand()

    playerHand = []
    playerHand.append(Hand())

    dealerPlay(dealerHand)

    complete = False
    x = 0

    while not complete:
	if len(playerHand) > x:
            splitHand = playerPlay(playerHand[x], dealerHand)

            if splitHand is "cont":
                x = x + 1
            else:
                playerHand.append(splitHand)
  	else:
	    complete = True

    print "\nDealer Hand:"
    print dealerHand.handValue()
    print dealerHand.hand
    print "\n"

    for x in range(len(playerHand)):
        print "Player 1 hand " + str(x)
        print playerHand[x].handValue()
        print playerHand[x].hand
        decideWinner(playerHand[x], dealerHand)
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

play()




#TODO
# look into passing to a split hand that it cannot acheive blackjack
# look into how to destroy objects to start a new hand
# look to reshuffle the cards when the shoe nears the end
# Look at better way of dealing with splits. If split is required pass back to play function and call playerPlay again with a new hand instance. PlayerHand becomes a list.
