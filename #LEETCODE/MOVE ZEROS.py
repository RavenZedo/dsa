#move zeros to end of array
#leetcode no. 283 = https://leetcode.com/problems/move-zeroes
nums = [1, 0, 2, 4, 3, 0, 0, 3, 5, 1]
n = len(nums)
i = 0
j=0
while j<n:
    if nums[j]!=0:
        nums[i],nums[j]=nums[j],nums[i]
        i+=1
    j+=1
print(nums)