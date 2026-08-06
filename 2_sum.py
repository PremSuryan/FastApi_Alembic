# Two Sum:
# nums = [2,7,11,15]
nums = [15,11,7,2]
target = 13


dic = {}
for i,v in enumerate(nums):
    comp = target - v
    if comp in dic:
        print([dic[comp], i])
        break

    dic[v] = i 

print(dic)


nums = [1,2,3,0,5]
# nums = [2, 1, -1]


total = sum(nums)
#print(total)
left = 0
right = 0
for i in range(len(nums)):
    right = total - left - nums[i]
    #right = total - left 
    #print(right)
    if left == right:
        print(i)
        break
    left += nums[i]
else:
    print(-1)
    

