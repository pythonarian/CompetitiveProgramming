class Stack:
    def __init__(self):
        self.stack = list()
        self.items = 0

    def push(self, item):
        self.stack.append(item)
        self.items += 1

    def pop(self):
        if not self.isEmpty():
            self.stack.pop()
            self.items -= 1
        else:
            print("Stack is already empty. Nothing can be popped.")

    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
            return

        print(self.stack[len(self.stack) - 1])
        return self.stack[len(self.stack) - 1]

    def isEmpty(self):
        if len(self.stack):
            return False
        else:
            return True

    def __len__(self):
        return self.items

# s = Stack()
# s.push(1)
# s.push(-5)
# s.peek()
# print(s.isEmpty())
# s.push('Asif')
# print(s.__len__())
# print(len(s))
# s.pop()
# s.pop()
# s.pop()
# print(s.isEmpty())
# print(s.__len__())
# print(len(s))
