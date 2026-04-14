#square of sorted array
#leetcode 977
nums = [-4,-1,0,3,10]
n=len(nums)
nums.sort()
for i in range(0,n):
    nums[i]=nums[i]**2
nums.sort()
print(nums)