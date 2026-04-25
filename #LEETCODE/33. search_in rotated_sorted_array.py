#search in rotated sorted array
#leetcode 33
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n=len(nums)
        l=0
        h=n-1
        while l<=h:
            mid=(l+h)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<=nums[h]:
                if nums[mid]<=target<=nums[h]:
                    l =mid+1
                else:
                    h=mid-1
            else:
                if nums[l] <=target<=nums[mid]:
                    h = mid -1
                else:
                    l=mid+1                  
        return -1
    