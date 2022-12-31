class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        ans = bin(a+b)
        return ans[2:]
        
#Runtime 38 ms Beats 80.42%
#Memory 13.8 MB Beats 71.66%
