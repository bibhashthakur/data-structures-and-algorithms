class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertathead(self, val):
        newnode = Node(val)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head = newnode

    def insertattail(self, val):
        newnode = Node(val)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode

    def insertafternode(self, where, what):
        newnode = Node(what)
        temp = self.head

        if temp == None:
            self.head = newnode
            self.tail = self.head
            return
        while (temp.val != where):
            temp = temp.next
        newnode.next = temp.next
        temp.next = newnode
        if newnode.next == None:
            self.tail = newnode

    def removefromhead(self):
        if self.head == None:
            return None
        val = self.head.val
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        return val

    def removefromtail(self):
        if self.head == None:
            return None
        val = self.tail.val
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            temp.next = None
            self.tail = temp
        return val

    def deletenode(self, val):
        if self.head == None:
            print('Empty List!')
        elif self.head.val == val:
            if self.head == self.tail:
                self.head, self.tail = None, None
            else:
                self.head = self.head.next
        else:
            slow = self.head
            fast = self.head.next
            while (fast != None) and (fast.val != val):
                fast = fast.next
                slow = slow.next
            if fast == None:
                print('Node not found')
                return
            slow.next = fast.next
            del fast

    def enumerate(self):
        temp = self.head
        count = 1
        print('')
        while temp != None:
            print(count, temp.val)
            temp = temp.next
            count += 1


def driver():
    ll = LinkedList()
    ll.insertafternode(2, 3)
    ll.enumerate()
    ll.insertafternode(3, 99)
    ll.enumerate()
    ll.insertafternode(3, 22)
    ll.enumerate()
    ll.insertafternode(99, 45)
    ll.enumerate()
    ll.insertattail(2222)
    ll.enumerate()

    ll.deletenode(23)
    ll.removefromhead()
    ll.enumerate()
    ll.removefromtail()
    ll.deletenode(22)
    ll.enumerate()
