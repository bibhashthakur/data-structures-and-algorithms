class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, val):
        newnode = Node(val)
        if self.top == None:
            self.top = newnode
        else:
            newnode.next = self.top
            self.top = newnode

    def pop(self):
        if self.top == None:
            print('Empty Stack')
            return None
        val = self.top.val
        self.top = self.top.next
        return val

    def peek(self):
        if self.top == None:
            print('Empty Stack')
            return None
        return self.top.val


def driver():
    st = Stack()
    print(st.pop())
    st.push(5)
    st.push(10)
    print(st.peek())
    print(st.pop())
    print(st.peek())
