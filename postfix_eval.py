#Ali Mohammed Shujjat - as03856 - L2 - Question 1

#For command line arguments
import sys
arglist = sys.argv[1:]

#Using stacks to pop operands with the operator
def postfix_eval(Expression):
    NumStack = []
    operators = ["+","-","*","/","^"]
    items = Expression.split()
    for i in items:
        if (isfloat(i)):
        	NumStack.append(i)
        if (i in operators):
            operand2 = NumStack.pop()
            operand1 = NumStack.pop()
            result = doMath(str(i),float(operand1),float(operand2))
            NumStack.append(result)
    return NumStack.pop()

#Function to return value after calculations
def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2
    elif op == "^":
        return op1 ** op2

#Function to check if string is of type float
def isfloat(value):
	try:
		float(value)
		return True
	except ValueError:
		return False

if (len(sys.argv) < 2):
        Exp = input("Please enter a postfix notation of an expression: ")
        print(postfix_eval(Exp))
else:
        for i in range(1,len(sys.argv)):
            print(postfix_eval(sys.argv[i]))
