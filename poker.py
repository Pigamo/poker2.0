
# Card
class Card:
    def __init__(self, rank,suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        return self.rank+self.suit
    def getRank(self):
        return self.rank
    def getSuit(self):
        return self.suit
    def value(self):
        return

# Score
class Score:
    def __init__(self):
        self.straight_flush = 0
        self.quad = 0
        self.straight = 0
        self.flush = 0
        self.test =0
        self.full_house =0
        self.trips = 0
        self.two_pair =0
        self.pair=0
        self.high_card =0
        self.super_straight = 0
        self.royal_flush=0
        self.scores=[]
    def setRoyalFlush(self):
        self.royal_flush +=1
    def setSuperStraight(self):
        self.super_straight +=1
    def setStraightFlush(self):
        self.straight_flush +=1
    def setTest(self):
        self.test +=1
    def setQuad(self):
        self.quad +=1
    def setStraight(self):
        self.straight +=1
    def setFlush(self):
        self.flush +=1
    def setFullHouse(self):
        self.full_house +=1
    def setTrips(self):
        self.trips +=1
    def setTwoPair(self):
        self.two_pair+=1
    def setPair(self):
        self.pair+=1
    def setHigh(self):
        self.high_card+=1
    def getScores(self):
        return [self.royal_flush,self.straight_flush,
            self.quad,
            self.full_house,
            self.flush,
            self.straight,
            self.trips,
            self.two_pair,
            self.pair,
            self.high_card]
    
    def __str__(self):
        total =f'Straight Flush: {self.straight_flush}\nQuad: {self.quad}\nFull House: {self.full_house}\nFlush: {self.flush}\nStraight: {self.straight}\n'
        total += 'Trips: ' + f'{self.trips}'
        total += '\nTwo pair: ' + f'{self.two_pair}'
        total += '\nPair: ' + f'{self.pair}'
        total += '\nHigh Card: ' + f'{self.high_card}'
        total += '\nSuper Straight ' + f'{self.super_straight}'
        total += '\nRoyal Flush ' + f'{self.royal_flush}'
        total += '\nTotal Hands:' + f'{self.straight_flush+self.quad+self.straight+self.flush+self.trips+self.full_house+self.two_pair+self.pair+self.high_card+self.super_straight+self.royal_flush}'
        return total


class Hand(Card):
    def __init__(self, cards):
        self.cards = cards
    def getCard(self):
        return self.cards
    def __str__(self):
        printout = ''
        for i in range(0,5):
            printout += translateCard(self.cards[i]) + self.cards[i].getSuit() + ' '
        return printout

import random


deck = ['1h','2h','3h','4h','5h','6h','7h','8h','9h','10h','11h','12h','13h',
        '1d','2d','3d','4d','5d','6d','7d','8d','9d','10d','11d','12d','13d',
        '1c','2c','3c','4c','5c','6c','7c','8c','9c','10c','11c','12c','13c',
        '1s','2s','3s','4s','5s','6s','7s','8s','9s','10s','11s','12s','13s']
rank=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
handNames = [
    "High Card",          # 0
    "One Pair",           # 1
    "Two Pair",           # 2
    "Three of a Kind",    # 3
    "Straight",           # 4
    "Flush",              # 5
    "Full House",         # 6
    "Four of a Kind",     # 7
    "Straight Flush",     # 8
    "Royal Flush"         # 9
]

def splitRankSuit(card):
    rank = card[:-1]
    suit = card[-1]
    return Card(rank,suit)
def checkNum(cards):
    nums = []
    for i in range(len(cards)):
        if i+1 < len(cards):
            num = cards[i+1] - cards[i]
            nums.append(num)
    return nums
def checkDubs(cards):
    nums = []
    for i in range(len(cards)):
        if i+1 < len(cards):
            num = cards[i+1] - cards[i]
            nums.append(num)
    return nums
def checkStraight(numbers):
    if numbers.count(1)==4:
        return True
def checkSuperStraight(numbers):
    if numbers[0]==9 and numbers.count(1)==3:
        return True

def checkFlush(cards):
    length = len(set(cards))
    if length <=1:
        return True
    
def checkQuad(cards):
    for i in range(0,1):
        if cards.count(cards[i])==4:
            return True
def checkForAces(cards):
    if 13 not in cards:
        return cards
    elif 1 in cards and 2 in cards:
        cards = cards[:-1]
        cards.insert(0,0)
def translateCard(card):
    return rank[int(card.getRank())-1]

def scoreHand(hand):
    cards = hand.getCard()
    ranks = []
    suits = []
    handValue = 0
    for i in range(0,5):
        rank = cards[i].getRank()
        ranks.append(int(rank))
        suit = cards[i].getSuit()
        suits.append(suit)
    ranks.sort()
    numbers = checkNum(ranks)
    if checkSuperStraight(numbers):
        if checkFlush(suits):
            score.setRoyalFlush()
            handValue = 9
            print("holy shit royal flush", hand)
        else:
            score.setSuperStraight()
            handValue = 4
    elif numbers.count(0)==3:
        if numbers[0] == 0 and numbers[3] == 0:
            score.setFullHouse()
            handValue = 6
        else:
            score.setQuad()
            handValue = 7
    elif checkStraight(numbers):
        if checkFlush(suits):
            score.setStraightFlush()
            handValue =8
        else:
            score.setStraight()
            handValue = 4
    elif checkFlush(suits):
        score.setFlush()
        handValue=5
    
    elif numbers.count(0)==2:
        
        if (numbers[0] ==0 and numbers[2]==0) or (numbers[1] == 0 and numbers[3]==0) or (numbers[0]==0 and numbers[3]==0):
            score.setTwoPair()
            handValue=2
        else:
            score.setTrips()
            handValue=3
    
    elif numbers.count(0)==1:
        score.setPair()
        handValue = 1
    else:
        score.setHigh()
        
    return handValue

    
def drawCards(newDeck):
    cards = []
    for i in range(5):
        index = random.randrange(0,len(newDeck))
        card_choice = newDeck[index]
        card = splitRankSuit(card_choice)
        newDeck.pop(index)
        cards.append(card)
    return cards
            




import matplotlib.pyplot as plt

def plotScores(counts, total):
    labels = [
        "Royal Flush",
        "Straight Flush",
        "Quad",
        "Full House",
        "Flush",
        "Straight",
        "Trips", 
        "Two Pair",
        "Pair",
        "High Card"
    ]

    percentage = [count / total * 100 for count in counts]

    
    bars = plt.bar(labels, counts)

    plt.xticks(rotation=45, ha='right')
    plt.ylabel("Count")
    plt.title(f'Poker Hand Frequencies of {total} Games')
    plt.tight_layout()
    plt.yscale("log")

    
    for bar, count, pct in zip(bars, counts, percentage):
        if count > 0:
            plt.text(
                bar.get_x() + bar.get_width() / 2,
                count,
                f'{count} \n{pct:.6f}%',
                ha='center',
                va='bottom',
                fontsize=8
            )

    plt.show()


def testGame(numGames):
    print(f'Running Simulation of {numGames} Poker Hands:\n')
    score = Score()
    for i in range(numGames):
        newDeck = list(deck)
        newHand = Hand(drawCards(newDeck))
        #print(f'Player {i+1}: ', newHand, '\n')
        scoreHand(newHand)
    #print(score)
    plotScores(score.getScores(),numGames)
    print('\nEnd of Sim')

#testGame(50000)


# Deal Game
from tabulate import tabulate
score = Score()

### Sets Silent Mode
silent = True
def silentPrint(text):
    if silent:
        return
    else: print(text)
def dealGames(numPlayers):
    
    silentPrint(f'{numPlayers} Player Game\n')
    newDeck = list(deck)
    gameTracker = []
    for i in range(numPlayers):
        newHand = Hand(drawCards(newDeck))
        scoredHand = scoreHand(newHand)
        #print(f'Player {i+1}: ', newHand,handNames[scoredHand], '\n')
        
       
        gameTracker.append({'player': f'Player {i+1}','score': scoredHand, 'name':handNames[scoredHand], 'hand': newHand})
    gameTracker.sort(key=lambda x: x['score'], reverse=True)
    # print(gameTracker)
    silentPrint(tabulate(gameTracker, headers="keys"))
    winner = gameTracker[0]
    silentPrint(f"\n| {winner['player']} WINS\n| With a {winner['name']}\n| {winner['hand']}")
    silentPrint('\nEnd\n')
def playMulti(numGames,numPlayers):
    print(f'\nSimulating {numGames} games with {numPlayers} players\n')
    for i in range(numGames):
        silentPrint(f'Game {i+1}')
        dealGames(numPlayers)
    totalHands = numGames * numPlayers
    plotScores(score.getScores(), totalHands)
#playMulti(1000,7)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--games", type=int, default=10)
    parser.add_argument("--players", type=int, default=5)
    args = parser.parse_args()
    playMulti(args.games, args.players)
