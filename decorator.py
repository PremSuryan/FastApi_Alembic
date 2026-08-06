def dec(f):
    def wrapper(args):
        print("start")
        f(args)
        print("End")

    return wrapper


@dec
def test(a):
    print("break " * 2)

# test(2)

#Add another decorator 

from functools import wraps

def dec(f):
    @wraps(f)
    def wrapper(args):
        print("Start")
        f(args)
        print("End")
    return wrapper


def another_dec(f):
    @wraps(f)
    def wrapper(args):  
        print("Before test")
        f(args)
        print("After test")
    return wrapper


@dec
@another_dec
def test(a):
    """Testing the decorator with the wrapper function """
    print("break" * 2)

test(2)
print(test.__name__)
print(test.__doc__)


