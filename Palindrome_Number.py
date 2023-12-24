class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        else:
            y = str(x)[::-1]
            if (x - int(y)) == 0:
                return True
            else:
                return False