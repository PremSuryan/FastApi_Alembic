# data = [
#     {"name": "DK", "marks": 88},
#     {"name": "Rahul", "marks": 90},
#     {"name": "Arun", "marks": 88},
#     {"name": "Priya", "marks": 95},
#     {"name": "Kumar", "marks": 90}
# ]
# new=[]
# dup =[]
# for d in data:
#     if d['marks'] not in new:
#         new.append(d['marks'])
#     else:
#         dup.append(d['marks'])
# dic={}
# for d in data:
#     if d['marks'] in dup and d['marks'] not in dic:
#         dic[d['marks']]= []
#     dic[d['marks']].append(d['name'])

# print(dic)



# data = [
#     {"name": "DK", "department": "MECH", "marks": 90},
#     {"name": "Rahul", "department": "EEE", "marks": 85},
#     {"name": "Arun", "department": "MECH", "marks": 88},
#     {"name": "Priya", "department": "CS", "marks": 95},
#     {"name": "Kumar", "department": "EEE", "marks": 82}
# ]

# """
# output = {
#     "MECH": ["DK", "Arun"],
#     "EEE": ["Rahul", "Kumar"],
#     "CS": ["Priya"]
# }
# """
# dic={}

# for d in data:
#     if d['department'] not in dic:
#         dic[d['department']] = []
#     dic[d['department']].append(d['name'])

# print(dic)