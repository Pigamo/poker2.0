import random
from typing import List
from tabulate import tabulate
from deck import create_deck, draw_cards,fulldeck
from hand import Hand
from score import Score
from plotter import plot_scores
from utils import sublist, checkStraight, checkSuperStraight, checkFlush, silent, silentPrint

class Hand_Identity(Hand):
	def __init__(self, hand: Hand):
		super().__init__(hand)
		self.ranks = [int(c.get_rank()) for c in hand.get_cards()]
		self.suits = [c.get_suit() for c in hand.get_cards()]
		self.sortedranks = self.ranks.sort()
		self.sublist = sublist(self.ranks)
		'''self.highcard = False
		self.pair = False
		self.two_pair = False
		self.trips = False
		self.straight = False
		self.flush = False
		self.fullhouse = False
		self.quads = False
		self.straight_flush = False
		self.royal_flush = False'''
		self.handvalue = 0
		self.hand_types = [
    "High Card", "One Pair", "Two Pair", "Three of a Kind",
    "Straight", "Flush", "Full House", "Four of a Kind",
    "Straight Flush", "Royal Flush"
]
	def handtype(self)-> bool:
		if (self.sublist.count(0)>=1) or (self.sublist.count(1) == 4) or (len(set(self.suits)) == 1) or ((self.sublist[0] == 9) and (numbers.count(1) == 3)):
			if self.sublist.count(0)>=1:
				if self.sublist.count(0) == 1:
					self.handvalue = 1
				elif self.sublist.count(0) == 2:
					if ((self.sublist[0]==0 and self.sublist[2]==0) or 
						(self.sublist[1]==0 and self.sublist[3]==0) or 
						(self.sublist[0]==0 and self.sublist[3]==0)):
						self.handvalue = 2
					else:
						self.handvalue = 3
				elif self.sublist.count(0) == 3:
					if self.sublist[0] == 0 and self.sublist[3] == 0:
						self.handvalue = 6
					else:
						self.handvalue = 7
			elif self.sublist.count(1) == 4:
				if len(set(self.sublist) == 1):
					self.handvalue = 8
				else:
					self.handvalue = 4
			elif (self.sublist[0] == 9) and (numbers.count(1) == 3):
				if len(set(self.sublist) == 1):
					self.handvalue = 9
				else:
					self.handvalue = 4
			else:
				self.handvalue = 5
		else:
			self.handvalue = 0
	def __str__(self)-> str:
		return f"{self.hand_types[self.handvalue]}"

deck = list(fulldeck)
newhand = Hand(draw_cards(deck))
handtype = Hand_Identity(newhand)
print(handtype)

def checkStraight(numbers: List[int]) -> bool:
    return numbers.count(1) == 4
def checkSuperStraight(numbers: List[int]) -> bool:
    return (numbers[0] == 9) and (numbers.count(1) == 3)
def checkFlush(suits: List[str]) -> bool:
    return len(set(suits)) == 1

def scored_hand(hand: Hand, score: Score) -> int:
	cards = hand.get_cards()
	ranks = [int(c.get_rank()) for c in cards]
	suits = [c.get_suit() for c in cards]
	ranks.sort()
	numbers = checkNum(ranks)
	handValue = 0

	if checkSuperStraight(numbers):
		if checkFlush(suits):
			score.set_royal_flush()
			handValue = 9
		else:
			score.set_super_straight()
			handValue = 8

	elif numbers.count(0) == 3:
		if numbers[0] == 0 and numbers[3] == 0:
			score.set_full_house()
			handValue = 6
		else:
			score.set_quad()
			handValue = 7

	elif checkStraight(numbers):
		if checkFlush(suits):
			score.set_straight_flush()
			handValue = 8
		else:
			score.set_straight()
			handValue = 4
	elif checkFlush(suits):
		score.set_flush()
		handValue = 5
	elif numbers.count(0) == 2:
		pairs = ((numbers[0]==0 and numbers[2]==0) or 
				(numbers[1]==0 and numbers[3]==0) or 
                 (numbers[0]==0 and numbers[3]==0))
		if pairs:
			score.set_two_pair()
			handValue = 2
		else:
			score.set_trips()
			handValue = 3
	elif numbers.count(0) == 1:
		score.set_pair()
		handValue = 1
	else:
		score.set_high()
		handValue = 0
	return handValue