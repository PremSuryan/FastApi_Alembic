arr =[1,1,1,0,1,1,1,1]


count = 1
max_count = 1

for i in range(1,len(arr)):
    if arr[i] == arr[i-1]:
        count += 1
    else:
        count = 1

    max_count = max(count, max_count)

print(max_count)