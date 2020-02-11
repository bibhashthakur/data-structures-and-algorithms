import numpy as np


class Stack:
    def __init__(self, datatype):
        #print("Datatype is ", datatype)
        self.arr = np.empty(5, dtype=datatype)
        self.top = -1
        self.size = self.arr.size

    def push(self, val):
        if (self.top == self.size - 1):
            self.size *= 2
            newarr = np.empty(self.size, dtype=int)
            for i in range(self.top + 1):
                newarr[i] = self.arr[i]
            self.arr = newarr

        self.top += 1
        self.arr[self.top] = val

    def pop(self):
        if self.top == -1:
            print('Stack is empty!')
            return
        val = self.arr[self.top]
        self.top -= 1
        return val

    def peek(self):
        if self.top == -1:
            print('Stack is empty!')
            return
        val = self.arr[self.top]
        return val


def driver():
    stack = Stack(int)
    print(stack.top)
    print(stack.size)
    stack.push(11)
    stack.push(22)
    stack.push(33)
    stack.push(44)
    stack.push(55)
    print(stack.top)
    print(stack.size)
    print(stack.pop())
    print(stack.peek())

    stack.push(66)
    print(stack.top)
    print(stack.size)
