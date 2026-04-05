#right rotate an array by 1 places
nums = [3,9,5,6,7,2]
n = len(nums)
temp = nums[n-1]
for i in range(n-2,-1,-1):
    nums[i+1]=nums[i]
nums[0]=temp
print(nums)