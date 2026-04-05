#REMOVE DUPLICATES FROM SORTED ARRAY

nums = [1,1,2,3,4,4,5,7,8,8,]
n =len(nums)
nums.sort()
i=0
j=i+1
while j<n:
    if nums[i]!=nums[j]:
        i+=1
        nums[i],nums[j]=nums[j],nums[i]
    j+=1
print(i+1)  