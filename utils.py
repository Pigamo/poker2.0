from collections import Counter
from typing import List
from card import Card

RANK_NAMES = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
silent = True
def silentPrint(text):
    if silent:
        return
    else: print(text)

def split_rank_suit(card_str: str) -> Card:
    rank_str = card_str[:-1]
    suit = card_str[-1]
    return Card(rank_str, suit)


def translate_card(card: Card) -> str:
    idx = int(card.get_rank()) - 1
    return RANK_NAMES[idx]


def checkNum(cards: List[int]) -> List[int]:
    nums = []
    for i in range(len(cards) - 1):
        nums.append(cards[i+1] - cards[i])
    return nums


def checkStraight(numbers: List[int]) -> bool:
    return numbers.count(1) == 4


def checkSuperStraight(numbers: List[int]) -> bool:
    return (numbers[0] == 9) and (numbers.count(1) == 3)


def checkFlush(suits: List[str]) -> bool:
    return len(set(suits)) == 1
