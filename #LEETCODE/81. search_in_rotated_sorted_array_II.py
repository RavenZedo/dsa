#leetcode 81
#search in rotated sorted array with duplicates
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        n=len(nums)
        l=0
        h=n-1
        while l<n:
            mid=(l+h)//2
            if nums[mid]==target:
                return True
            elif nums[l]==nums[mid]==nums[h]:
                l += 1
                h -= 1
                continue
            elif nums[mid]<nums[h]:
                if nums[mid]<=target<=nums[h]:
                    l=mid+1
                else:
                    h=mid-1
            else:
                if nums[l]<=target<=nums[mid]:
                    h=mid-1
                else:
                    l=mid+1
        return False

            