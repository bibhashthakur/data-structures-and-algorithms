class Node:
    def __init__(self, val, prior):
        self.val = val
        self.next = None
        self.priority = prior


class PriorityQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, val, prior):
        newnode = Node(val, prior)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
            return

        slow = self.head
        fast = self.head.next
        #print(val, slow.val, fast.val)
        while(fast != None and fast.priority < prior):
            #print(fast.val, slow.val)
            print(self.peek())
            fast = fast.next
            slow = slow.next

        newnode.next = fast
        slow.next = newnode
        if fast == None:
            self.tail = newnode

    def dequeue(self):
        if self.head == None:
            print('Empty Queue')
            return None

        val = self.head.val
        if self.head == self.tail:
            self.head = None
            self.tail = None

        else:
            self.head = self.head.next
        return val

    def peek(self):
        if self.head == None:
            print('Empty Queue')
            return None

        return (self.head.val, self.tail.val)


def driver():
    pq = PriorityQueue()
    print(pq.dequeue())
    print(pq.peek())

    pq.enqueue(11, 1)
    print(pq.peek())
    print(pq.dequeue())
    print(pq.peek())

    pq.enqueue(11, 3)
    pq.enqueue(14, 1)
    pq.enqueue(72, 2)
    print(pq.peek())


driver()
