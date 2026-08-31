"""
c = a^2 + b^2
c = 5
output True
explanation : 1^1 + 2^2 = 1+4 = 5 so true

ex 2:
c =3 
output = False

"""

# 5 --> 1 + 4, 2 + 3 , 0 + 5
c = 7
found= False
for i in range(c+1):
    for j in range(i,c+1):
        if i*i + j*j == c:
            print(True)
            found = True
            break

    if found:
        break

if not found:
    print(False)