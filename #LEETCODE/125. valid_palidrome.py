#valid palidrome
#leetcode 125
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pali=""
        for i in s:
            if i.isalnum():
                pali+=i.lower()
        return pali==pali[::-1] 