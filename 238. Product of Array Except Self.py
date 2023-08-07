class Solution:
    def productExceptSelf(self, nums) :
        n=[1]*len(nums)
        
        premulti=1
        postmulti=1
        for i in range(len(nums)):
            n[i] *= premulti
            premulti *= nums[i]
            n[len(nums)-i-1] *= postmulti
            postmulti *=  nums[len(nums)-i-1]
        
        return n
        
        
        
sol = Solution

# premulti --->
nums=[3,2,1,6]
#            <-----postmulti
# with each time solutin is updated from above and from the back
r = sol.productExceptSelf(sol,nums)
