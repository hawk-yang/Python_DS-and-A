import timeit

def popzero():
    x.pop(0)

def popend():
    x.pop()


x = list(range(2000000))

print(timeit.timeit("popzero()", "from __main__ import popzero", number = 1000)," milliseconds")
print(timeit.timeit("popend()", "from __main__ import popend", number = 1000)," milliseconds")
