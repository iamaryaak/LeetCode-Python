class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # each move: +1 or -1
        # first thing: find the avg between all numbers, and +1 or -1 from other elements to match it
        # ex: [1, 10, 2, 9] : avg = (1+10+2+9)/4 = 22 // 4 = 5
        # another approach: 1, 2, 9, 10: get median: 5, 4+3+4+5 = 16
        # [1,0,0,8,6] = 0,0,1,6,8 = median = 4
        # 4, 5, 3, 4 = 16
        # ex: [1, 2, 3] : avg = (1+2+3)/3 = 2
        # 1, 0, 1 = 2
        
        # find the median in the array***        
        avg = 0
        nSum = 0
        # sort array
        nums = sorted(nums)
        medianEl = nums[len(nums)//2]
        
        # inc/dec
        totalMoves = 0
        for i in range(len(nums)):
            indMove = (nums[i] - medianEl)
            if indMove < 0:
                indMove*=-1
            totalMoves += indMove
        return totalMoves
