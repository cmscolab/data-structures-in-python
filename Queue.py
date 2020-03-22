class Queue:
    def __init__(self, head=None):
        self.items = [head]

    def dequeue(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def enqueue(self, item):
        self.items.append(item)


if __name__ == '__main__':
    q = Queue(1)
    q.enqueue(2)
    q.enqueue(3)

    # Test peek
    # Should be 1
    print q.peek()

    # Test dequeue
    # Should be 1
    print q.dequeue()

    # Test enqueue
    q.enqueue(4)
    # Should be 2
    print q.dequeue()
    # Should be 3
    print q.dequeue()
    # Should be 4
    print q.dequeue()
    q.enqueue(5)
    # Should be 5
    print q.peek()