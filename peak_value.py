vals = [3, 4, 5, 1, 2]

for i in range(1,len(vals)-1):
    if vals[i] > vals[i-1] and vals[i]>vals[i+1]:
        print(vals[i])
    else:
        continue


