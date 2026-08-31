""" Reverse the string with and without slicing """

x = '1534236469'
# with slicing :

print(x[::-1])


#Without Slicing :


x = list(x)

left = 0
right = len(x) - 1

while left < right:
    x[left], x[right] =  x[right],x[left]
    left +=1
    right -=1

print("".join(x))