class Solution:
    def buildArray(self, nums): 
        s=[]
        for i in range(len(nums)):
            s.append(nums[nums[i]])
        return s             