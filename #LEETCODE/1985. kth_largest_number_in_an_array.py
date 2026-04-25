#kth largest number in an array
#leetcode 1985
class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        nums = ["3","6","7","10"]
        k = 4
        nums.sort(key=lambda x: (int(x),x))
        return nums[-k]
solution = Solution()
print(solution.kthLargestNumber(["3","6","7","10"],4))
        
    