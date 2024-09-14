class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        small = min(a, b)
        big = max(a, b)
        res = 0
        for i in range(1, small + 1):
            if (small % i == 0) and (big % i == 0):
                res = res + 1
        return res
    
        