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


from Code_4_5 import Stack # As previously defined
def infix_to_postfix(infix_expr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    op_stack = Stack()
    output = []
    character_list = infix_expr.split()

    for character in character_list:
        if character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or character in "0123456789":
            output.append(character)
        
        elif character == '(':
            op_stack.push(character)
            
        elif character == ')':
            top_token = op_stack.pop()
            while top_token != '(':
                output.append(top_token)
                top_token = op_stack.pop()
        
        else:
            while (not op_stack.is_empty()) and \
            (prec[op_stack.peek()] >= prec[character]):
                output.append(op_stack.pop())
            
            op_stack.push(character)

    while not op_stack.is_empty():
        output.append(op_stack.pop())
    return " ".join(output)

print(infix_to_postfix("A * B + C * D"))
print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))



