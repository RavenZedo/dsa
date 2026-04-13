#max consecutive ones in an array
#leetcode 485
def max_consecutive(nums):
    max_count = 0
    count = 0
    for i in nums:
        if i == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count
max_consecutive([1,1,0,1,1,1])