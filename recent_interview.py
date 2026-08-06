matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [15,16,17]
]

#output = [1, 2, 3, 4, 8, 11, 12, 9, 10, 5, 6, 7, 15, 16, 17]


out = []
out.extend(matrix[0]) 
out.extend([matrix[1][-1]])
out.extend(matrix[2][2:]+matrix[2][0:2])
out.extend(matrix[1][0:3]+matrix[3])

print(out)

