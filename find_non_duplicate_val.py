arr = [2,3,5,3,2,1]
#output = 5   [2,3,5,3,2,1]
# arr.sort()
# print(arr)
left = 0
right = len(arr) - 1
out=[]
while left < right:
    if arr[left] == arr[right]:
        left +=1
        right -=1

    elif arr[left] in out and arr[right] in out:
        left +=1
        right -=1
        continue
    else:
        out.extend([arr[left],arr[right]])
        left +=1
        right -+1

    if left == right:
        out.append(arr[left])

# print(out)



#Method 2:
arr = [2,3,5,3,2,1]

out=[]
for i in arr:
    if arr.count(i) == 1:
        out.append(i)

print(out)


#Using xor operator

arr = [2,3,5,3,2,1]

ans = 0

for num in arr:
    ans ^= num

# print(ans)