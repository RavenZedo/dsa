#260. Single Number III
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        result = []
        for num, count in freq.items():
            if count == 1:
                result.append(num)

        return result