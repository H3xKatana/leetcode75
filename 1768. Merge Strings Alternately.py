class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
            z=""
            for i in range(min(len(word1),len(word2))):
               z += word1[i]+word2[i]
            x=i
            if len(word1) > len(word2):
                z += word1[x+1:]
            if len(word1) < len(word2):
                z += word2[x+1:]
            return z
                
       