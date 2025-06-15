from typing import List

class Score:
    def __init__(self):
        self.royal_flush = 0
        self.straight_flush = 0
        self.quad = 0
        self.full_house = 0
        self.flush = 0
        self.straight = 0
        self.trips = 0
        self.two_pair = 0
        self.pair = 0
        self.high_card = 0
        self.super_straight = 0

    def set_royal_flush(self):   self.royal_flush += 1
    def set_super_straight(self): self.super_straight += 1
    def set_straight_flush(self): self.straight_flush += 1
    def set_quad(self):           self.quad += 1
    def set_full_house(self):     self.full_house += 1
    def set_flush(self):          self.flush += 1
    def set_straight(self):       self.straight += 1
    def set_trips(self):          self.trips += 1
    def set_two_pair(self):       self.two_pair += 1
    def set_pair(self):           self.pair += 1
    def set_high(self):           self.high_card += 1

    def get_scores(self) -> List[int]:
        return [
            self.royal_flush,
            self.straight_flush,
            self.quad,
            self.full_house,
            self.flush,
            self.straight,
            self.trips,
            self.two_pair,
            self.pair,
            self.high_card
        ]

    def __str__(self) -> str:
        lines = [
            f"Royal Flush: {self.royal_flush}",
            f"Straight Flush: {self.straight_flush}",
            f"Four of a Kind: {self.quad}",
            f"Full House: {self.full_house}",
            f"Flush: {self.flush}",
            f"Straight: {self.straight}",
            f"Trips: {self.trips}",
            f"Two Pair: {self.two_pair}",
            f"Pair: {self.pair}",
            f"High Card: {self.high_card}",
            f"Super Straight: {self.super_straight}",
        ]
        total = sum(self.get_scores())
        lines.append(f"Total Hands: {total}")
        return "\n".join(lines)
