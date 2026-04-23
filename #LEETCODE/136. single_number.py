#single number
#leetcode 136
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sets=set()
        n=len(nums)
        count=0
        i=0
        for i in range(0,n):
            if nums[i] not in sets :
                sets.add(nums[i])
            else:
                sets.remove(nums[i])
        return sets.pop()  