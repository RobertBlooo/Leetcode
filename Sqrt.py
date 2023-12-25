class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        while True:
            if i*i < x:
                i += 1
            elif i*i == x:
                return i
            else:
                return i-1