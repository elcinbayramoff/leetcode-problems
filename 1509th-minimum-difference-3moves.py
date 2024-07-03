class Solution:
    def minDifference(self, nums: list[int]) -> int:

        nums.sort()
        length = len(nums)
        if length <= 4:
            return 0
        else:
            return min(nums[length-4]-nums[0], nums[length-3]-nums[1], nums[length-2]-nums[2], nums[length-1]-nums[3])