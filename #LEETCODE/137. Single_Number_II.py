#137. Single Number II
class Solution(object):
    def singleNumber(self, nums):
        nums.sort()

        i = 0
        while i < len(nums) - 1:
            if nums[i] != nums[i + 1]:
                return nums[i]
            i += 3

        return nums[-1]