# Sorting :

"""
you have two types of sorting :
1. bubble sort 
2. selection sort
3. merge sort
"""

#bubble sort 

numbers = [5, 3, 8, 2]
n = len(numbers)
for i in range(n):
    for j in range(n -i -1):
        if numbers[j]>numbers[j+1]:
            numbers[j],numbers[j+1] = numbers[j+1], numbers[j]

print(numbers)


#Selection Sort :
numbers = [64, 25, 12, 22, 11]
n=len(numbers)

for i in range(n):
    min_index = i

    for j in range(i+1, n):
        if numbers[j]<numbers[min_index]:
            min_index = j

    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

print(numbers)


#Insertion Sort 
arr = [12, 11, 13, 5, 6]

n=len(arr)

for i in range(1,n):
    key = arr[i]
    j= i-1

    while j>= 0 and arr[j] > key:
        arr[j+1] = arr[j]
        j-=1


    arr[j+1] = key


print(arr)  


#Merge Sort:

