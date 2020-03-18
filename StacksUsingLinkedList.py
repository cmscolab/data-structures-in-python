class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_ele):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_ele
        else:
            self.head = new_ele

    def insert_first(self, new_ele):
        new_ele.next = self.head
        self.head = new_ele

    def delete_first(self):
        if self.head:
            del_ele = self.head
            temp = self.head.next
            self.head = temp
            return del_ele
        else:
            return None

class Stack(object):
        def __init__(self, top=None):
            self.ll = LinkedList(top)

        def push(self, value):
                self.ll.insert_first(value)

        def pop(self):
            return self.ll.delete_first()


if __name__ == '__main__':
    # Test cases
    # Set up some Elements
    e1 = Node(1)
    e2 = Node(2)
    e3 = Node(3)
    e4 = Node(4)

    # Start setting up a Stack
    stack = Stack(e1)

    # Test stack functionality
    stack.push(e2)
    stack.push(e3)
    print stack.pop().value
    print stack.pop().value
    print stack.pop().value
    print stack.pop()
    stack.push(e4)
    print stack.pop().value