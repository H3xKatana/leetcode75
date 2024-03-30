class Solution:
    def pivotIndex(self, nums) -> int:
        leftsum=0
        rightsum=sum(nums)
        for i in range(len(nums)):
            rightsum -= nums[i]
            if rightsum == leftsum :
                return i
            
            leftsum += nums[i]
            
            
        return -1