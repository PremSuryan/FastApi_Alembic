#Get duplicate element :

arr = [2,3,4,1,1,2,7]

val = [i for i in arr if arr.count(i) > 1]
print(val)