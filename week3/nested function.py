def fn3(x):
    return x + 1

def fn2(func, val1):
    def inner(val2):
        return func(val1) + val2
    return inner

def fn1(func, val2):
    return func(val2)

b = int(input())
c = int(input())

a = fn1(fn2(fn3, b), c)
print(a)