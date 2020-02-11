from linkedlist import LinkedList


class Queue:

    def __init__(self):
        self.ll = LinkedList()

    def enqueue(self, val):
        self.ll.insertattail(val)

    def dequeue(self):
        return self.ll.removefromhead()

    def peek(self):
        if self.ll.head == None:
            return None
        return self.ll.head.val


q = Queue()
print(q.dequeue())
print(q.peek())
q.enqueue(55)
q.enqueue(33)
print(q.dequeue())
print(q.peek())
