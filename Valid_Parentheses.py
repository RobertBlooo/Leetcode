class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            "(":")",
            "[":"]",
            "{":"}"
        }
        ls = list()
        for i in s:
            if i in dic:
                ls.append(i)
            elif len(ls) == 0 or i != dic[ls.pop()]:
                return False
        return len(ls) ==0