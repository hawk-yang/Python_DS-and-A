import random

from Code_4_5 import Stack

stack = Stack()

for i in range (5):
    stack.push(random.randint(0, 100))


print(stack.items)

def ParChecker(inputString):
    stack = Stack()

    for i in inputString:
        if i == '(':
            stack.push(i)
        elif i == ')':
            stack.pop()
    if stack.isEmpty():
        return True
    else:
        return False

print(ParChecker("(())()"))