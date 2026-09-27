arr = [1,1,1]
k1=2

arr2=[1,1,1,2,1,2,3] 
k2 =3

def sub_array(arr,k):
    result = []
    current = []

    for num in arr:
        if num == k:
            result.append([num])
        current.append(num)

        if sum(current) == k:
            result.append(current)
            current=[]



    return result

print(sub_array(arr2,k2))

new_arr = [1, 2, 3, 4, 5, 6, 7, 8,9]
k = 3

for i in range(0, len(new_arr), k):
    new = new_arr[i:i + k]
    print(new)


subarrays = [new_arr[i:i + k] for i in range(0, len(new_arr), k)]

print(subarrays)


