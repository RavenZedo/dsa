#descending order
nums=[1,7,8,4,5,6,9,2]
def func(nums):
    n=len(nums)
    for i in range(0,n):
        max_index=i
        for j in range(i+1,n):
            if nums[j]>nums[max_index]:
                max_index=j
        nums[i],nums[max_index]=nums[max_index],nums[i]
func(nums)
print(nums)
