#771. Jewels and Stone
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s=0
        for i in jewels:
            for x in stones :
                if i in x :
                    s += 1
        return s 