#find minimum in rotated sorted array
#leetcode 153
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=[3,1,2,4,5]
        n=len(nums)
        l=0
        h=n-1
        min_val=float('inf')
        while l<=h:
            mid=(l+h)//2
            if nums[mid]<=nums[h]:
                min_val=min(min_val,nums[mid])
                h=mid-1
            else:
                min_val=min(min_val,nums[l])
                l=mid+1
        return min_val
    solution = Solution()   
    print(solution.findMin([3,1,2,4,5]))