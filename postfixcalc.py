from stackarray import Stack
import numpy as np


def postfixcalc(expression):

    stack = Stack(int)
    expression = expression.split(' ')
    # print(stack.arr.dtype)
    for i in expression:
        # print(i)
        if i == ' ':
            pass
        elif i == '+':
            op2 = int(stack.pop())
            op1 = int(stack.pop())
            stack.push(op1 + op2)
        elif i == '-':
            op2 = int(stack.pop())
            op1 = int(stack.pop())
            stack.push(op1 - op2)
        elif i == '*':
            op2 = int(stack.pop())
            op1 = int(stack.pop())
            stack.push(op1 * op2)
        elif i == '/':
            op2 = int(stack.pop())
            op1 = int(stack.pop())
            stack.push(op1 / op2)
        elif i == '%':
            op2 = int(stack.pop())
            op1 = int(stack.pop())
            stack.push(op1 % op2)
        else:
            stack.push(int(i))
            # print(stack.peek())
    return stack.pop()


print(postfixcalc("5 6 7 * + 10 -"))
