class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        rep = 1 
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                nums[rep] = nums[i]
                rep += 1
        return rep
