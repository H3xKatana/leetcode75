from math import gcd
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l=gcd(len(str1),len(str2))
        if str1+str2 == str2+str1:
            return str1[:l]
        else:
            return ""
        
        
#so first the length of the return string is equal to gcd of the lenghts
#we check if we can devide the strings if s1+s2==s2+s1
#then we return str with length of gcd