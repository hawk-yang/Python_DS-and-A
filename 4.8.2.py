from pythonds.basic import Stack

resultStack = Stack()
resultString = ""
digits = "0123456789ABCDEFGHIJKLMNOP"

def decToBin(dec, base):
    while dec != 0:
        resultStack.push(dec % base)
        dec //= base

decToBin(26, 26)

print(resultStack.items)
for i in range(len(resultStack.items)):
    resultString += str(digits[resultStack.items.pop()])

print(resultString)