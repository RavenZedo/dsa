#2nd largest element in array
largest =float('-inf')
second_largest = float('-inf')
nums=[55,32,97,45,-55,32,88,21]
n = len(nums)
for i in range(0,n):
    if nums[i]>largest:
        second_largest = largest
        largest = nums[i]
    elif nums[i]>second_largest and nums[i]!=largest:
        second_largest = nums[i]
print(second_largest)
