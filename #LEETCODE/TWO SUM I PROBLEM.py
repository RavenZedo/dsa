#TWO SUM PROBLEM

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums= [2,7,11,15]
        target=9
        result = []
        n=len(nums)
        for i in range(0,n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    result.append(i)
                    result.append(j)
        return result
solution = Solution()
print(solution.twoSum([2,7,11,15],9))