"""
All elements less than the pivot go to the left.
The pivot stays in the middle.
All elements greater than the pivot go to the right.

For your array:

arr = [2, 3, 13, 15, 21, 10, 1, 0, 5]
pivot = 10

the expected result can be:

[2, 3, 5, 1, 0, 10, 21, 15, 13]

(The order of elements on each side doesn't matter, only that they're on the correct side.)
"""



arr = [2, 3, 13, 15, 21, 10, 1, 0, 5]

pivot = 10

#Method 1:

# Move pivot to the end
pivot_index = arr.index(pivot)
arr[pivot_index], arr[-1] = arr[-1], arr[pivot_index]

left = 0
right = len(arr) - 2  # Ignore the pivot at the end

while left <= right:

    while left <= right and arr[left] < pivot:
        left += 1

    while left <= right and arr[right] > pivot:
        right -= 1

    if left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

# Place the pivot in its correct position
arr[left], arr[-1] = arr[-1], arr[left]

print(arr)


#Method 2:
find_index = arr.index(pivot)
pop_index_value = arr.pop(find_index)
arr.append(pop_index_value)
print(arr)