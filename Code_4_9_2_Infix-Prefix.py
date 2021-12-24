#My initial attempt at a solution
# input = "(3+(5*7))"
# operators = Stack ()
# characters= ["QWERTYUIOPASDFGHJKLZXCVBNM1234567890"]
# output = []

# def conversion(input):
#     for i in input:
#         if(i == "("):
#             operators.push(i)
#         elif(i in characters):
#             output.append(i)
#         elif():
#             top = operators.peek()
#             while top != "(":
#                 output.append(operators.pop())


from Code_4_5 import Stack

opstack = Stack()
output = []
inputString = "(((A+B)*C)+D)"



for i in range(len(inputString)):
    if(inputString[i] == "("):
        opstack.push(inputString[i])
    elif(inputString[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or inputString[i] in "1234567890"):
        output.append(inputString[i])

    elif(inputString[i] == ")"):
        while(opstack.peek() != "("):
            output.append(opstack.pop())
        if(opstack.peek() == "("):
            opstack.pop()

#Print output 