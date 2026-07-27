# find the largest number:

numbers = [5, 3, 10, 2, 8]

largest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i
    continue

print(largest)


