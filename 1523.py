class Solution:
    def countOdds(self, low: int, high: int) -> int:
        res = 0
        if low % 2 == 0:
            if high % 2 == 0:
                # 2, 3, 4, 5, 6, 7, 8
                # 3, 5, 7
                res = (high - low)//2
            else:
                # 2, 3, 4, 5, 6, 7
                # 3, 5, 7
                res = (high - low)//2 + 1
        else:
            if high % 2 == 0:
                # 3, 4, 5, 6, 7, 8
                # 3, 5, 7
                res = (high - low)//2 + 1
            else:
                # 3, 4, 5, 6, 7
                # 3, 5, 7
                res = (high - low)//2 + 1

        return res
