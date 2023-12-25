class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        
        triangle = self.generate(numRows-1)
        pre = triangle[-1]
        new = [1]

        for i in range(1, len(pre)):
            new.append(pre[i-1] + pre[i])
        new.append(1)
        triangle.append(new)
        return triangle