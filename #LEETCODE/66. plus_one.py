#plus one to a number represented as an array
#leetcode 66
def plusOne(nums):
    n=len(nums)
    for i in range(n-1,-1,-1):
        if nums[i]<9:
            nums+=1
            return nums
        else:
            nums[i]=0
    else:
        return nums + [1]              
    



