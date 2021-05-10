"""
Stack Data Structure

Assuming we have books A B C D on the floor. Let's stack em.

D
C
B
A

We can then take books from the top of the stack.
LIFO
We push stuff onto stack; we pop stuff off the stack.
"""


class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items


s = Stack()
s.push("A")
s.push("B")

print(s.get_stack())

s.push("C")
print(s.get_stack())

s.pop()
print(s.get_stack())

s.push("C")
print(s.peek())
