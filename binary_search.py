#Types of search :

#1. Linear Search
numbers = [2, 5, 8, 10, 14, 20, 25, 31]
target = 20

for i in range(len(numbers)):
    if numbers[i] == target:
        print(i)

    continue
print(-1)




#Binary Search 


numbers = [2, 5, 8, 10, 14, 20, 25, 31]
target = 20

left = 0
right = len(numbers)-1

middle = left + right // 2

while left <= right:
    if numbers[middle] == target:
        print(middle)

    elif left < middle:
        right = middle - 1

    else:
        left = middle + 1

print(-1)