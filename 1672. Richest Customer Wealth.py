class Solution:
    def maximumWealth(self, accounts) -> int:
    
       return max(sum(row) for row in accounts)
       