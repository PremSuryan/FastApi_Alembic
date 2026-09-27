nums=[1,2,3,4,5]
iterator = iter(nums)

try:
    while True:
        print(next(iterator))

except StopIteration:
    pass


"""
Defination of the iteration:

iteration means going through items one by one


"""

"""
Defination of the iterators:

An iterator is a object that gives you the item one at a time
"""


"""
Defination of the Generator:
generator is a much easier way of creating an iterator
uses  :  yeild instead of return the value
"""
from collections import Counter

nums= [1, 2, 3, 2, 4, 6, 4]

count = Counter(nums)

dup = [k for k,v in count.items() if v>1]
print(dup)
