class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        bas = strs[0]
        for i in range(len(bas)):
            for j in strs[1:]:
                if (i == len(j) or j[i] != bas[i]):
                    return bas[0:i]
        return bas