#rearrange array in alternating positive and negative items
#leetcode 2149

nums = [3,1,-2,-5,2,-4]
positive = []
negative = []
for num in nums:
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)
result = []
i = 0
j = 0
while i < len(positive) and j < len(negative):
    result.append(positive[i])
    result.append(negative[j])
    i += 1
    j += 1
print(result)    
