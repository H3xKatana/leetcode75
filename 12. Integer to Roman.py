class Solution:
    def intToRoman(self, num: int) -> str:
        roman_Nums = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1
        }
        roman_str = ""

        for key, val in roman_Nums.items():
            while num >= val:
                roman_str += key
                num -= val

        return roman_str
              
solu=Solution
num=1800
r=solu.intToRoman(solu,num)
print(r)
"""I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.""" 