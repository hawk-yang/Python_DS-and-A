from Code_4_5 import Stack

def ParChecker(inputString):
    stack = Stack()
    openers = "([{"
    closers = ")]}"

    for i in range(len(inputString)):

        print("Stack starting state for i =", i, stack.items)

        if inputString[i] in openers:
            stack.push(inputString[i])

        elif closers.index(inputString[i]) == openers.index(stack.peek()):
            stack.pop()
        
        else:
            
            return False


    if stack.isEmpty():
        return True
    else:
        return False

print(ParChecker('{({([][])}())}'))