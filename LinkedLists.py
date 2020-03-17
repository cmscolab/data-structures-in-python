class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head):
        self.head = head

    def append(self, new_ele):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_ele
        else:
            self.head = new_ele

    def get_value_at_position(self, position):
        current = self.head
        counter = 1
        if position < 1:
            return None
        while current and counter <= position:
                if counter == position:
                    return current
                current = current.next
                counter += 1
        return None

    def insert(self, new_ele, position):
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_ele.next = current.next
                    current.next = new_ele
                current = current.next
                counter += 1
        elif position == 1:
            new_ele.next = self.head
            self.head = new_ele

    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next

if __name__ == '__main__':
    # Test cases
    # Set up some Elements
    e1 = Node(1)
    e2 = Node(2)
    e3 = Node(3)
    e4 = Node(4)

    # Start setting up a LinkedList
    ll = LinkedList(e1)
    ll.append(e2)
    ll.append(e3)

    # Test get_position
    # Should print 3
    print ll.head.next.next.value
    # Should also print 3
    print ll.get_value_at_position(3).value

    # Test insert
    ll.insert(e4, 3)
    # Should print 4 now
    print ll.get_value_at_position(3).value

    # Test delete
    ll.delete(1)
    # Should print 2 now
    print ll.get_value_at_position(1).value
    # Should print 4 now
    print ll.get_value_at_position(2).value
    # Should print 3 now
    print ll.get_value_at_position(3).value