import openpyxl

file_path = r'E:\Fast Api Alembic\Project-Management-Sample-Data.xlsx'

with open(file_path,'rb') as f:
    workbook = openpyxl.load_workbook(f)

    sheet = workbook.active

    for i in sheet.iter_rows(values_only = True):
        # print(i)
        pass


import pandas as pd

df = pd.read_excel(file_path,skiprows=4)

print(df.to_dict(orient='list'))