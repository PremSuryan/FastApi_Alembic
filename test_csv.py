import pandas as pd

file_path= r'E:\Fast Api Alembic\people-100.csv'

df = pd.read_csv(file_path)
res = df[df['Job Title']=="Games developer"]
# print(res)


import random

res= []
matrix1 = [[round(random.random(),2) for _ in range(1,4)] for _ in range(1,4)]
# matrix2 = [random.random() for i in range(1,4)]
# matrix3 = [random.random() for i in range(1,4)]

res.append(matrix1)
# res.append(matrix2)
# res.append(matrix3)
print(res)