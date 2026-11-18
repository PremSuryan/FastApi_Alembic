def test():
    yield 1
    yield 2
    yield 3


g = test()

print(next(g))
print("Hi")

import time

time.sleep(5)
print("Hieiei")

print(next(g))

time.sleep(10)
print("end")


print(next(g))

# from collections import defaultdict,deque
# from concurrent.futures import ThreadPoolExecutor

# def func():
#     print("Thread start")
#     import time
#     time.sleep(10)
#     print("Thread End")


# with ThreadPoolExecutor(max_workers=1) as ex:
#     print("Future start")
#     future = ex.submit(func)
#     print("Future End")



# lst = [1,2,3,4,5,6,7]
# dq = deque(lst)
# dq.rotate(3)
# print(dq)


# dic = defaultdict(dict)
# dic['key1'].update({"Akey":"Hello"})
# dic['key1'].update({"Bkey":"World"})

# print(dic)



# dic['key1'].append("Hello")
# dic['key1'].append("World")
# dic['key2'].append("World")


# print(dic)


# class ABC():
#     pass


# a=ABC()
# a.first = 'Hello'
# a.second = 'World!'

# print(a.__dict__)