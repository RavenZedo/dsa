#check if array is sorted or not


def func(nums):
    nums=[1,1,6,8,9]
    n=len(nums)
    for i in range(0,n-1):
        if nums[i]>nums[i+1]:
            return False
        
    return True
func('nums')