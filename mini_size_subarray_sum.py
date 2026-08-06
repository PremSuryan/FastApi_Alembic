arr = [2,3,1,2,4,3]
target = 7

#output = [4,3]

found = False
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] + arr[j] == target:
            print([i,j])
            found =True
            break
    if found:
        break


def two_sum(arr, target):
    seen = {}

    for i , v in enumerate(arr):
        diff = target - v
        print(diff)
        if diff in seen:
            print(seen)
            return [seen[diff], i]

        seen[v] = i


print(two_sum(arr,target))