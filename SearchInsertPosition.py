class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[-1] < target:
                return len(nums)
            if nums[i] >= target:
                return i