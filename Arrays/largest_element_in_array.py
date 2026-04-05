nums=[1, 7, 8, 4, 5, 6, 9, 2]
n=len(nums)
largest = float('-inf')
for i in range(0,n):
    if nums[i]>largest:
        largest=nums[i]
print(largest)