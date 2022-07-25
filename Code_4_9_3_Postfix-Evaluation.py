from Code_4_5 import Stack # As previously defined

def evaluate_postfix(postfix_expr):
    prec = {
        "*": 3, "/": 3, "+": 2, "-": 2, "(": 1
        }

    operand_stack = Stack()
    output = []
    character_list = postfix_expr.split()
    print(character_list)

    for character in character_list:
        if character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or character in "0123456789":
            operand_stack.push(character)
        
        elif character in "*/+-" and :
            swap1 = operand_stack.pop()
            swap2 = operand_stack.pop()
            operand_stack.push(str(eval(swap2 + character + swap1)))
        
        else:
            for i in range(len(operand_stack.items)):
                output.append(operand_stack.pop())
            print(output)

    return " ".join(output)

print(evaluate_postfix("7 8 + 3 2 + /"))
