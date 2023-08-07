class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        
        second = max(nums)+1
        first=second 
        
        for third in nums :
            
            
            if third > second :
                return True
            if third <= first :
                first=third
            else:
                second=third
        return False        
    # first second third presents an triplet
    # IF THIRD IS BIGGER THAN SECOND IT MEANS WE FOUND A FULL TRIPLET
    # IF THIRD IS SMALLER THAN FIRST WE MAKE FIRTST EQUAL TO THIRD
    # IF THIRD IS SMALLER THAN OR EQUAL TO SECOND WE MAKE SECOND = THIRD and the loop keep going