class Stack:
    def __init__(self):
        self.stack = []

    # Push operation: Adds an element to the top of the stack
    def push(self, value):
        self.stack.append(value)

    # Pop operation: Removes and returns the top element from the stack
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty!"

    # Peek operation: Returns the top element without removing it
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty!"

    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Get the current size of the stack
    def size(self):
        return len(self.stack)

# Example usage:
my_stack = Stack()
my_stack.push(10)       # Stack: [10]
my_stack.push(20)       # Stack: [10, 20]
my_stack.push(30)       # Stack: [10, 20, 30]

print("Current Stack:", my_stack.stack)    # Output: [10, 20, 30]
print("Top Element:", my_stack.peek())     # Output: 30
print("Popped Element:", my_stack.pop())   # Output: 30
print("Stack After Pop:", my_stack.stack)  # Output: [10, 20]