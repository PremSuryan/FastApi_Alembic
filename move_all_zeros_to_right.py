arr = [1, 0, 2, 0, 3, 0, 4, 5]

# move zero to the right 
res_right = [i for i in arr if i!=0] + [0] * arr.count(0)
print(res_right)

# move zero to the left 

res_left = [0] * arr.count(0) + [i for i in arr if i!=0]
print(res_left)