#bubble sort DESCENDING ORDER
nums = [5, 8, 1, 6, 9, 2, 4]
def bubble_sort(nums):
    n=len(nums)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if nums[j]>nums[i]:
                nums[i],nums[j]=nums[j],nums[i]
bubble_sort(nums)
print(nums)