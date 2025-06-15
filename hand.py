from typing import List
from card import Card
from utils import translate_card

class Hand:
    def __init__(self, cards: List[Card]):
        self.cards = cards

    def get_cards(self) -> List[Card]:
        return self.cards

    def __str__(self) -> str:
        return " ".join(f"{translate_card(c)}{c.suit}" for c in self.cards)
