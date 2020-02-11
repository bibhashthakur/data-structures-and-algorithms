import numpy as np


class Queue:
    def __init__(self, datatype=int):
        self.arr = np.empty(3, dtype=datatype)
        self.head = -1
        self.tail = -1
        self.size = self.arr.size

    def enqueue(self, val):
        if self.head == -1:
            self.head += 1
            self.tail += 1

        elif (self.tail + 1) % self.size == self.head:
            newarr = np.empty(self.size * 2, dtype=self.arr.dtype)

            newidx = 0
            for i in range(self.head, self.size):
                newarr[newidx] = self.arr[i]
                newidx += 1
            if self.head != 0:
                for i in range(self.tail+1):
                    newarr[newidx] = self.arr[i]
                    newidx += 1

            del self.arr
            self.arr = newarr
            self.head = 0
            self.tail = self.size
            self.size *= 2

        else:
            self.tail = (self.tail + 1) % self.size

        self.arr[self.tail] = val

    def dequeue(self):
        if self.head == -1:
            print('Queue is empty')
            return None
        val = self.arr[self.head]
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
            return val

        self.head = (self.head + 1) % self.size
        return val

    def peek(self):
        if self.head == -1:
            print('Queue is empty')
            return None
        return self.arr[self.head]

    def printstats(self):
        print("Array size: ", self.arr.size, " Head: ",
              self.head, " Tail: ", self.tail)


def driver1():
    q = Queue()
    q.printstats()
    q.dequeue()
    q.peek()

    q.enqueue(3)
    q.enqueue(1)
    q.printstats()

    q.enqueue(7)
    q.enqueue(4)
    q.printstats()

    print(q.dequeue())
    q.printstats()
    print(q.peek())
    q.printstats()

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    q.printstats()


def driver2():
    q = Queue()
    q.enqueue(11)
    q.enqueue(22)
    q.enqueue(33)
    q.printstats()

    print(q.dequeue())
    print(q.dequeue())

    q.enqueue(44)
    q.printstats()

    q.enqueue(55)
    # q.enqueue(66)
    q.printstats()

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())


driver2()
