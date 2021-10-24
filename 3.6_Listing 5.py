import timeit

def popzero():
    x.pop(0)

def popend():
    x.pop()


print("pop(0)   pop()")

for i in range(1000000,100000001,1000000):
    x = list(range(i))
    pt = timeit.timeit("popend()", "from __main__ import popend", number=1000)
    pz = timeit.timeit("popzero()", "from __main__ import popzero", number=1000)
    print("%10.5f, %15.5f" %(pz,pt))