class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class doublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def AddFirst(self, val):
        newnode = Node(val)

        if self.head == None:
            self.head, self.tail = newnode, newnode
        else:
            self.head.prev = newnode
            newnode.next = self.head
            self.head = newnode

    def AddLast(self, val):
        newnode = Node(val)

        if self.head == None:
            self.head, self.tail = newnode, newnode
        else:
            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode

    def RemoveFirst(self):
        if self.head == None:
            print('Can\'t delete. Empty List')
            return

        if self.head == self.tail:
            self.head, self.tail = None, None
        else:
            self.head.next.prev = None
            self.head = self.head.next

    def RemoveLast(self):
        if self.head == None:
            print('Can\'t delete. Empty List')
            return

        if self.head == self.tail:
            self.head, self.tail = None, None
        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev

    def Remove(self, val):
        if self.head == None:
            print('Can\'t delete. Empty List')
            return

        if self.head == self.tail:
            if self.head.val == val:
                self.head, self.tail = None, None
            else:
                print('Element not present')
                return
        else:
            temp = self.head
            while (temp != None) and (temp.val != val):
                temp = temp.next
            if temp == None:
                print('Element not present')
                return
            if temp.prev != None:
                temp.prev.next = temp.next
            if temp.next != None:
                temp.next.prev = temp.prev
            del temp

    def enumeratefromstart(self):
        temp = self.head
        count = 1
        print('From beginning:')
        while temp != None:
            print(count, temp.val)
            temp = temp.next
            count += 1

    def enumeratefromend(self):
        temp = self.tail
        count = 1
        print('From end:')
        while temp != None:
            print(temp.val)
            temp = temp.prev
            count += 1


ll = doublyLinkedList()
ll.AddFirst(5)
ll.enumeratefromstart()
ll.enumeratefromend()
ll.AddFirst(7)
ll.AddFirst(9)
ll.enumeratefromstart()
ll.enumeratefromend()

ll.AddLast(10)
ll.AddLast(15)
ll.enumeratefromstart()
ll.enumeratefromend()

ll.RemoveFirst()
ll.RemoveLast()
ll.Remove(5)
ll.enumeratefromstart()
ll.enumeratefromend()
ll.Remove(9)
ll.enumeratefromstart()
ll.enumeratefromend()
ll.Remove(10)
ll.enumeratefromstart()
ll.RemoveLast()
ll.Remove(15)
ll.enumeratefromstart()
ll.enumeratefromend()
ll.Remove(7)
ll.enumeratefromstart()
ll.enumeratefromend()
