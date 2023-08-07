class Solution:
    def reverseWords(self, s: str) -> str:
        x=[]
        g=""
        for i in range(len(s)):
            if s[i] != " " :
                g += s[i] 
            elif  g != ""   :
                x.insert(0,g)
                g= ""
        if g != "":
            x.insert(0,g)
                
        

        return " ".join(x)

sol = Solution
s="hello   world is "
r=sol.reverseWords(sol,s)
print(r)

