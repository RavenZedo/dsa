#rearrange array in alternating positive and negative items
#leetcode 2149

def rearrangeArray(self, nums):
    n = len(nums)
    result = [0] * n
    pos = 0
    neg = 1
    for i in range(n):
        if nums[i] >= 0:
            result[pos] = nums[i]
            pos += 2
        else:
            result[neg] = nums[i]
            neg += 2
    return result
 
