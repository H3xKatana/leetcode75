'''
1512
easy 
hashmaps

Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

'''
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        x=0
        for i in range(len(nums)):
            for j in range(len(nums)-1):

                if (nums[i] == nums[j]) and (i < j):
                    x +=1
        return x


  