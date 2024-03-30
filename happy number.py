"""
happy number problem leetcode 202
hash table 
easy
A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 
"""
class Solution:
    def isHappy(self, n: int) -> bool:
        set_of_no=set()
        while n!=1: 
            n=sum([int(i)**2 for i in str(n)])
            if n in set_of_no: 
                return False 
            set_of_no.add(n)
        return True

        
