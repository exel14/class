class Stack:
    """Custom class for pythom Stack"""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == 0

    def push(self,x):
        self.items.append(x)

    def delete(self):
        self.items.pop()

    def size(self):
        return len(self.items)

    def take(self):
        return self.items[-1]
    #take берет первый элемент сверху

stack = Stack()
for i in range(8):
    stack.push(i)
stack.delete()
print(stack.size())
print(stack.take())
print(stack.items)