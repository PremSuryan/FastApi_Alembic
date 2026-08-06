arr = [0,0,1,1,1,2,2,3,3,4]

seen = set()
res = []

for i in arr:
    if i not in seen:
        seen.add(i)
        res.append(i)

print(res)