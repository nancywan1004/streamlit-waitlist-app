class Node(object):
    # Constructor to initilize class variables
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def getLength(self):
        length = 0
        temp = self.head
        while (temp != None):
            length += 1
            temp = temp.next
        return length

    def insertAtBeginning(self, data):
        temp = Node(data)
        if self.head == None:
            self.head = temp
        else:
            temp.next = self.head
            self.head = temp

    def insertAtEnd(self, data):
        temp = Node(data)
        if self.head == None:
            self.head = temp
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = temp

    def insertAtGivenPosition(self, data, position):
        count = 1
        curr = self.head
        while count < position-1 and curr != None:
            curr = curr.next
            count += 1
        temp = Node(data)
        temp.next = curr.next
        curr.next = temp

    def traverse(self):
        curr = self.head
        while curr != None:
            print(curr.data)
            curr = curr.next

    def delFromBeginning(self):
        try:
            if self.head == None:
                raise Exception("Empty Linked List")
            else:
                temp = self.head
                self.head = self.head.next
                del temp
        except Exception as e:
            print(str(e))

    def delFromEnd(self):
        try:
            if self.head == None:
                raise Exception("Empty Linked List")
            else:
                curr = self.head
                prev = None
                while curr.next != None:
                    prev = curr
                    curr = curr.next
                prev.next = curr.next
                del curr
        except Exception as e:
            print(str(e))

    def delAtPos(self, position):
        try:
            if self.head == None:
                raise Exception("Empty Linked List")
            else:
                curr = self.head
                prev = None
                count = 1
                while curr != None and count < position:
                    prev = curr
                    curr = curr.next
                    count += 1
                prev.next = curr.next
                del curr
        except Exception as e:
            print(str(e))
