import matplotlib.pyplot as plt
from typing import List

HAND_NAMES = [
    "Royal Flush",
    "Straight Flush",
    "Four of a Kind",
    "Full House",
    "Flush",
    "Straight",
    "Trips",
    "Two Pair",
    "Pair",
    "High Card"
]

def plot_scores(counts: List[int], total: int):
    labels = HAND_NAMES
    percentages = [c / total * 100 for c in counts]
    bars = plt.bar(labels, counts)
    plt.xticks(rotation=45, ha='right')
    plt.ylabel("Count")
    plt.title(f"Poker Hand Frequencies of {total} Games")
    plt.tight_layout()
    plt.yscale("log")

    for bar, count, pct in zip(bars, counts, percentages):
        if count > 0:
            plt.text(
                bar.get_x() + bar.get_width() / 2,
                count,
                f"{count}\n{pct:.6f}%",
                ha='center', va='bottom', fontsize=8
            )
    plt.show()
