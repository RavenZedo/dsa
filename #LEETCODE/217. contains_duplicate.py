#contains duplicate
#leetcode 217

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sets=set()
        for i in nums:
            if i in sets:
                return True
            sets.add(i)    
        return False  