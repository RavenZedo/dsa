#longest consecutive sequence in an array
nums = [100, 4, 200, 1, 3, 2]
my_set = set()
n=len(nums)
for i in range(n):
    my_set.add(nums[i])
longest=0
for num in my_set:
    if num-1 not in my_set:
        current_num = num
        count=1  
        while current_num+1 in my_set:
            current_num+=1
            count+=1  
            longest = max(longest, count)
