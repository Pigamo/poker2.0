import random
from typing import List
from card import Card
from utils import split_rank_suit
fulldeck = ['1h','2h','3h','4h','5h','6h','7h','8h','9h','10h','11h','12h','13h',
        '1d','2d','3d','4d','5d','6d','7d','8d','9d','10d','11d','12d','13d',
        '1c','2c','3c','4c','5c','6c','7c','8c','9c','10c','11c','12c','13c',
        '1s','2s','3s','4s','5s','6s','7s','8s','9s','10s','11s','12s','13s']
RANKS = [str(i) for i in range(1, 14)]
SUITS = ["h", "d", "c", "s"]

def create_deck() -> List[str]:
    return [r + s for r in RANKS for s in SUITS]

def draw_cards(deck: List[str], count: int = 5) -> List[Card]:
    new_deck = deck.copy()
    cards: List[Card] = []
    for _ in range(count):
        code = random.choice(new_deck)
        new_deck.remove(code)
        cards.append(split_rank_suit(code))
    return cards
