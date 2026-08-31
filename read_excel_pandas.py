import json
import pandas as pd

excel_file_path = r"E:\Fast Api Alembic\Project-Management-Sample-Data.xlsx"


df = pd.read_excel(excel_file_path)
# df = df.to_string(index=False)
# print(df.head(7))

# header = 0
# not_value = 0
# for i , r in df.iterrows():
#     for value in r:
#         print(value)
#         while pd.isna(value):
#             not_value += 1
#         while not_value < len(df.columns):
#             header += 1

header = 0

for i, r in df.iterrows():
    not_value = 0

    for value in r:
        if pd.isna(value):
            not_value += 1

    if not_value > 2:
        header = i
        # break

# print("Header row:", header)

data = df.iloc[header+1:].to_dict(orient='list')
print(data)
import csv
with open('output.csv','w',newline='',encoding='utf-8') as f:
    writer = csv.DictWriter(f , fieldnames=df.columns)

    writer.writeheader()
    writer.writerows(data)



name_filer = df[df['Assigned to'].str.startswith('A')]
name_filer.drop(columns=['Unnamed: 0'], inplace=True)
print(name_filer)


df['Start Date'] = pd.to_datetime(df['Start Date'])
filter_df = df[df['Start Date'].dt.day == 1]
print(filter_df.to_dict(orient='list'))


dic = {}
for i,r in df.iterrows():
    print(i)
    print(r)

    for i, r in df.iterrows():
        for col in df.columns:
            if col == 'Unnamed: 0':
                continue
            if col not in dic:
                dic[col] = []
            if r[col] == None:
                continue
            dic[col].append(r[col])

print(dic)

    # if r['Project Name'] == 'Financial':
    #     fin_data.append(r)


# fin_data = df[df['Project Name'] == 'Financial']
# df = fin_data.drop(columns=['Unnamed: 0'])

# print(df)

# dic = {}

# for i, r in df.iterrows():
#     for value in r:
#         if value not in dic:
#             dic[value] = []
#         for k,v in dic.items():
#             if r==v and k!=r:
#                 dic[r].append(v)


# dic = {}

# for col in df.columns:
#     # dic[col] = dic[col].tolist()
#     dic[col] = []
#     for v in df[col].values:            
#         dic[col].append(v)


dic = {}

for col in df.columns:
    if col in ['Start Date', 'End Date']:
        dic[col] = [x.to_pydatetime() for x in df[col]]
    elif col == 'Days Required':
        dic[col] = [int(x) for x in df[col]]
    else:
        dic[col] = df[col].tolist()



print(dic)

dic = df.to_dict(orient='list')

# print(dic)

 