arr = [2,1,5,1,3,2]

k= 3
# max_sum = sum(arr[:k])
max_sum = 0
n = len(arr)
for i in range(n-k+1):  #6-3+1 ==4 (0,4)
    total = 0
    for j in range(i,i+k): #(0,3) -->(1,4)
        total += arr[j]

    if total > max_sum:
        max_sum = total     

print(max_sum)



#If i need to return the subarray too:
arr = [1,0,1,2,7,3,5]

n = len(arr)
k =3
max_sum, max_start = 0, 0
for i in range(n-k+1):  #0,5
    total = 0
    for j in range(i,i+k): #0,3
        total = total + arr[j]
    
    if total > max_sum:
        max_sum = total
        max_start = i
        
        
print(max_sum)
print(arr[max_start:max_start+k])
        

