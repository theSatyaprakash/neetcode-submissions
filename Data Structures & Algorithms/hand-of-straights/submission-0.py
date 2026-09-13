from collections import Counter
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        for card in sorted(count):
            if count[card] > 0:
                freq = count[card]

                for x in range(card, card + groupSize):
                    if count[x] < freq:
                        return False

                    count[x] -= freq

        return True