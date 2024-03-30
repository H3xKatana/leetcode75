class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        j=s.sort()
        k=t.sort()
        if s.length() != t.length():
            return False
        
        if j != k :
            return  False
        else :
            return True
        