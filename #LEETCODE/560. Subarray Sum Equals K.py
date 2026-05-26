#560. Subarray Sum Equals K
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_sum = 0
        count = 0
        prefix_sum_count = {0: 1}
        for num in nums:
            prefix_sum+=num
            if prefix_sum-k in prefix_sum_count:
                count+=prefix_sum_count[prefix_sum-k]
            prefix_sum_count[prefix_sum]=prefix_sum_count.get(prefix_sum,0)+1
        return count