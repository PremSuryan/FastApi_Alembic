arr = [1,1,1]
k1=2

arr2=[1,2,3] 
k2 =3

def sub_array(arr,k):
    result = []
    current = []

    for num in arr:
        current.append(num)

        if sum(current) == k:
            result.append(current)
            current=[]


    return result

print(sub_array(arr2,k2))