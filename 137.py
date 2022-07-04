class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # bitwise manipulation
        # no extra space 
        # Time: O(n)
        
        one, two = 0, 0
        third = 0
         
        for i in nums:
            two = two ^ (one & i)
            one = one ^ i
            third = ~(one & two)
            two = two & third
            one = one & third
    

        return one
