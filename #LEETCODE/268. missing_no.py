#find the missing no. in array 
#leetcode 268

def missing(nums):
    n = len(nums)
    total_sum = n  * (n + 1) // 2
    actual_sum = sum(nums)
    return total_sum - actual_sum
missing([0,1,3])