class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n != 1:
            # appearing twice means its going around in circles
            if n in s:
                return False
            
            # else add it to the set
            s.add(n)
            
            # update n to be the sum of all it's digits
            total = 0
            for i in str(n):
                total += int(i) ** 2
            n = total
        return True
