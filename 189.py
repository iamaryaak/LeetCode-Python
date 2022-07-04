class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        subNums = nums[0:(len(nums)-k)]
        subNums1 = nums[(len(nums)-k):len(nums)]
        copy = (subNums1 + subNums)
        nums = copy
        print(nums)
        
        This solution does not work because nums is created as a new variable (not the same as nums from input)
        """
        
        # this is why we need a new solution
        # get length of remaining elements
        rE = k%len(nums)
        
        # 1, 2, 3, 4, 5 k = 2
        # 1, 2, 3  4, 5 would be the split and rE would leave 3 (len of 1, 2, 3)
        
        def rev(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                
                # increment
                start+=1
                end-=1
        
        # use rev on the 2 parts of the array
        nums.reverse()
        rev(0, rE-1)
        rev(rE, len(nums)-1)
        
            
