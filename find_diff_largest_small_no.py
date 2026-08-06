arr = [25,46,11,13,69]

n=len(arr)


for i in range(n):
    left = 0

    while left < len(arr) - 1:
        if arr[left] > arr[left + 1]:
            arr[left], arr[left + 1] = arr[left + 1], arr[left]

        left += 1
print(arr)


print(arr[-1]-arr[0])


    
