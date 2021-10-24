import null as null
from pythonds.basic import Stack

resultStack = Stack()
resultString = ""

def decToBin(decimal):
    while decimal != 0:
        resultStack.push(decimal % 2)
        decimal //= 2

decToBin(233)

print(resultStack.items)
for i in range(len(resultStack.items)):
    resultString += str(resultStack.items.pop())

print(resultString)
