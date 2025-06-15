import random
from typing import List
from tabulate import tabulate
from deck import create_deck, draw_cards,fulldeck
from hand import Hand
from score import Score
from plotter import plot_scores
from utils import checkNum, checkStraight, checkSuperStraight, checkFlush, silent, silentPrint

HAND_NAMES = [
    "High Card", "One Pair", "Two Pair", "Three of a Kind",
    "Straight", "Flush", "Full House", "Four of a Kind",
    "Straight Flush", "Royal Flush"
]

def score_hand(hand: Hand, score: Score) -> int:
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



def deal_game(num_players: int, score: Score):
    silentPrint(f'{num_players} Player Game\n')
    deck = list(fulldeck)
    gameTracker: List[dict] = []
    
    for i in range(num_players):
        newHand = Hand(draw_cards(deck))
        scoredHand = score_hand(newHand, score)
        #print(f'Player {i+1}: ', newHand,handNames[scoredHand], '\n')
        
       
        gameTracker.append({'player': f'Player {i+1}','score': scoredHand, 'name':HAND_NAMES[scoredHand], 'hand': newHand})
    gameTracker.sort(key=lambda x: x['score'], reverse=True)
    # print(gameTracker)
    silentPrint(tabulate(gameTracker, headers="keys"))
    winner = gameTracker[0]
    silentPrint(f"\n| {winner['player']} WINS\n| With a {winner['name']}\n| {winner['hand']}")
    silentPrint('\nEnd\n')


def play_multi(num_games: int, num_players: int):
    score = Score()
    print(f'\nSimulating {num_games} games with {num_players} players\n')
    score = Score()
    for i in range(num_games):
        silentPrint(f'Game {i+1}')
        deal_game(num_players, score)
    total_hands = num_games * num_players
    plot_scores(score.get_scores(), total_hands)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--games", type=int, default=1000)
    parser.add_argument("--players", type=int, default=7)
    parser.add_argument("--silent", type=bool, default=True,help="Run in silent mode")
    args = parser.parse_args()
    play_multi(args.games, args.players)
    silent = args.silent
