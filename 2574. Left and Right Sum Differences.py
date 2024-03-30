#2574. Left and Right Sum Differences
class Solution:
    def leftRightDifference(self, nums) -> [int]:
        result=[]
        for i in range(len(nums)):  
           result.append(abs(sum((nums[:i]))-(sum(nums[i+1:]))))
        return result
        
        pass
nums=[2,3,4,5,6]
print(nums[:0])


"""_summary_
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        rightSum=[total - nums[0]]
        leftSum=[total - rightSum[0] - nums[0]]
        result =[abs(rightSum[0]-leftSum[0])]
        
        for i in range(len(nums)-1):
            rightSum.append(rightSum[i]-nums[i+1])
            leftSum.append(total - rightSum[i+1] - nums[i+1])

            result.append(abs(rightSum[i+1]-leftSum[i+1]))
        
        return result
        """