class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=("a","e","i","o","u","A","E","I","O","U")
        x=[]
        l=list(s)
        for  i in range(len(s)):
            if s[i] in vowels:
                x.append(s[i])
      
        
        for i in range(len(s)):
            if s[i]  in vowels :
                l[i]=x.pop()
        
        s="".join(l)
        return s
        
    