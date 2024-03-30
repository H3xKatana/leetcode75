class Solution:
    def romanToInt(self, s: str) -> int:
        roman_Nums= {
       "M": 1000, 
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1,
        }
        
        g=0
        
        for i in range(len(s)):
            if i < len(s)-1 and  roman_Nums[s[i]]<roman_Nums[s[i+1]]:
                g -= roman_Nums[s[i]]
            else:
                g += roman_Nums[s[i]]
            
            
        return g
    
    
sol= Solution
s="MDCCC"
r=sol.romanToInt(sol,s)
print(r)

    