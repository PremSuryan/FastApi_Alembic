matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

#output 
'''
[
    [1,4,7],
    [2,5,8],
    [3,6,9]
]
'''
# res = []
# for i in range(len(matrix)):
#     for j in range(i,len(matrix)):
#         for k in range(j,len(matrix)):
#             # print(i,j,k)
#             if i==j==k:
#                 res.append([matrix[0][i],matrix[1][i],matrix[2][i]])
#             else:
#                 continue

# print(res)

#given below is the correct 
res = [list(x) for x in zip(*matrix)]
print(res)
