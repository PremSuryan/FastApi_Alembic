#Patterns Star

"""
Star pattern 
******
*****
****
***
**
*
"""
n=6
for i in range(n):
    for j in range(i+1,n):
    #     print("*",end="")
    # print()
        pass


"""
Star pattern
*
**
***
****
*****
"""
n=6
for i in range(1,n+1):
    # print("*" * i)
    pass
    
"""
Star parttern 
    *
   * *
  * * *
 * * * *
* * * * * 
  """

n=5
for i in range(n):
    for j in range(n-i-1):
        # print(" ",end="")
        pass

    for j in range(i+1):
        # print("* ",end="")
        pass


    # print()


n=5
for i in range(n):
    # print(" "*(n-i-1), end="")
    # print("* "*(i+1))
    pass



"""
Inverted Star pattern

* * * * *
 * * * *
  * * *
   * *
    *
"""

n=6
for i in range(n):
    print(" "*i, end="")  

    for j in range(i+1,n):
        print("* ",end="")

    print()

    