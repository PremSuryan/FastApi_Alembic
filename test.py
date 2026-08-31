num=12101

rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    print(rev)
    num=num//10
    
# print(rev)


flat=[1,[2,3],[4,5,6],[7,8],[9,10,11,13]]

# result =[j for i in flatten for j in i ]
# print(result)


def flatten(nested):
    res=[]
    for i in nested:
        if isinstance(i,list):
            res.extend(flatten(i))

        else:
            res.append(i)

    return res


# print(flatten(flat))


num =[1,2,3,5,7]

missing=[]
left =0

while left<len(num)-1:
    if num[left]+1 == num[left+1]:
        left+=1

    else:
        missing.append(num[left]+1)
        left+=1
# print(missing)


seq=[1,1,1,0,1,1,1,1,1]
res =1

for i in range(len(seq)-1):
    if seq[i]==seq[i+1]:
        res+=1
        
    else:
        res=1
        
# print(res)


#remove duplicate:
nums=[1,2,3,1,4,1,5]


# print(list(set(nums)))
# print(dict.fromkeys(nums))
# print(list(dict.fromkeys(nums)))



#Pivot Index:

nums = [1, 7, 3, 6, 5, 6]

#output : 3

left=0
total = sum(nums)
for i in range(len(nums)):
    right = total - left - nums[i]
    if left == right:
        print(i)
        break
    left += nums[i]

