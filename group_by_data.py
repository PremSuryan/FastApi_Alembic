data = [
    {"name":"ps", "age":30},
    {"name":"dk", "age":50},
    {"name":"surya", "age":30},
    {"name":"shan", "age":30}

]

"""
output:
res = [
[
    {"name":"ps", "age":30},
    {"name":"surya", "age":30},
    {"name":"shan", "age":30}
],
[
    {"name":"dk", "age":50},

]
]
"""

res = []


for val in data:
    found = False

    for i in res:
        if i[0]["age"] == val["age"]:
            i.append(val)
            found = True
            break

    if not found:
        res.append([val])

print(res)