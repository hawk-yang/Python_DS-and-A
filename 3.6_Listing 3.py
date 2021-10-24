import timeit

def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))


print(timeit.timeit("test1()", setup="from __main__ import test1", number = 1000)," milliseconds")
print(timeit.timeit("test2()", setup="from __main__ import test2", number = 1000)," milliseconds")
print(timeit.timeit("test3()", setup="from __main__ import test3", number = 1000)," milliseconds")
print(timeit.timeit("test4()", setup="from __main__ import test4", number = 1000)," milliseconds")

