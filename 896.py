class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        res = 0
        
        # 1, 2, 3 - TRUE
        # 3, 2, 1 - TRUE
        # 1, 3, 2 - FALSE
        # 1, 1, 2 - TRUE
        # 1, 1, 0 - TRUE
        
        # keep track of how many sames, inc, dec in an array
        same = 0
        dec = 0
        inc = 0
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                dec+=1
            elif nums[i] > nums[i+1]:
                inc+=1
            else:
                same+=1
        if dec == 0:
            return True
        elif inc == 0:
            return True
        else:
            return False
