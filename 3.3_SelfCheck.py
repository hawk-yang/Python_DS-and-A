import random
import time

def returnMin_quadratic(nums):
    min = nums[0]
    for i in range(len(nums)):
        for j in range(len(nums)):
            if (nums[i] < min and nums[i] < nums [j] ):
                min = nums[i]
    return min


def returnMin_linear(nums):
    min = nums[0]
    for i in range(len(nums)):
        if(nums[i] < min ):
            min = nums[i]
    return min


ordersOfMagnitude = [1000, 10000, 1000]
for listSize in range(1000, 10000, 1000):
    randList = [random.randint(0,100000) for x in range(listSize)]
    start= time.time()
    print(returnMin_quadratic(randList))
    end = time.time()
    print("Runtime is: %f, while the size of the list is: %d" %(end-start,listSize) )

print("-------------------------------------------------")
for listSize in range(1000, 10001, 1000):
    randList = [random.randint(0,100000) for x in range(listSize)]
    start= time.time()
    print(returnMin_linear(randList))
    end = time.time()
    print("Runtime is: %f, while the size of the list is: %d" %(end-start,listSize) )
