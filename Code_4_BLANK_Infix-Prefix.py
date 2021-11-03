input = "(3+(5*7))"
operators = Stack ()
characters= ["QWERTYUIOPASDFGHJKLZXCVBNM1234567890"]
output = []

def conversion(input):
    for i in input:
        if(i == "("):
            operators.push(i)
        elif(i in characters):
            output.append(i)
        elif():
            top = operators.peek()
            while top != "(":
                output.append(operators.pop())



