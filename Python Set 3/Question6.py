# 1. **Implement Stack using Queue**: Use Python's queue data structure to implement a stack.
#     - *Input*: push(1), push(2), pop(), push(3), pop(), pop()
#     - *Output*: "1, None, 3, None, None"


from queue import Queue

class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, item):
        self.q2.put(item)  # Add the item to the second queue

        # Move all elements from the first queue to the second queue
        while not self.q1.empty():
            self.q2.put(self.q1.get())

        # Swap the references of q1 and q2
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if not self.q1.empty():
            return self.q1.get()
        else:
            return None

# Example usage
stack = Stack()

stack.push(1)
stack.push(2)
print(stack.pop())  # Output: 2

stack.push(3)
print(stack.pop())  # Output: 3
print(stack.pop())  # Output: 1
