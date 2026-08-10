class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            left, right = 0, 0
            if i == 0:
                right = sum(nums[i+1:])
            elif i == len(nums)-1:
                left = sum(nums[0:i])
            else:
                left = sum(nums[0:i])
                right =sum(nums[i+1:])
            if left == right:
                return i
        return -1
            

            