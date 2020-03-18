class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        #print(self.items[0])
        return self.items.pop(0)

    def isEmpty(self):
        return len(self.items) == 0

if __name__ == '__main__':
    stack = Stack()

    # Test stack functionality
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print stack.pop()
    print stack.pop()
    print stack.pop()
    stack.push(4)
    print stack.pop()