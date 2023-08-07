class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        m= max(candies)
        k=[]
        for i in range(len(candies)):
            if  (candies[i]+extraCandies) >=  m :
                k.append(True)
            else:
                k.append(False)
        return k
        