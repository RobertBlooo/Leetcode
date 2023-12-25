class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ls = s.split(' ')
        i = -1
        while True:
            if ls[i] != '':
                return len(ls[i])
            else:
                i -= 1