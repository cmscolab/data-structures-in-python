class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        return None
    def peek(self):
        if len(self.items) > 0:
            return self.items[-1]
        return None

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