#common element in the different array :


arr1=[1,2,3,4,5]
arr2=[7,8,9,3,5]
arr3=[6,1,0,3,5]


common = []
for i in arr1:
    if i in set(arr2) and i in set(arr3):
        common.append(i)

print(common)