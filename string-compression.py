class Solution:
    def compress(self, chars):
        n=0
        x=chars[0]
        s=""
        for  i in chars:
            if i == x:
                n +=1
            else:
                if n==1:
                    s +=x
                else:
                    s +=x
                    s +=str(n)
                x=i
        return s
        pass