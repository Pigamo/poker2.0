# Card
class Card:
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit

    def __str__(self) -> str:
        return f"{self.rank}{self.suit}"

    def get_rank(self) -> str:
        return self.rank

    def get_suit(self) -> str:
        return self.suit

    def value(self):
      
        pass
