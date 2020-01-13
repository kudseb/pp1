'''
class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def is_empty(self):
        return len(self.stack)==0
    def __str__(self):
        for i in self.stack[::-1]:
            print(i)
        return ''

x=Stack()
x.push(10)
x.push(4)
x.push(5)
x.push(3)
x.push(22)
print(x)
x.pop()
print(x)
x.pop()
print(x)
x.pop()
'''
class Queue:

    def __init__(self):
        self.stack = []

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop(0)

    def push(self, item):
        self.stack.append(item)

    def is_empty(self):
        return len(self.stack)==0
    def __str__(self):
        for i in self.stack:
            print(i)
        return ''
x=Queue()
x.push(10)
x.push(4)
x.push(5)
x.push(3)
x.push(22)
print(x)
x.pop()
print(x)
x.pop()
print(x)
x.pop()