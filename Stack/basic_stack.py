# Basic Stack implementation using Python list

stack = []

# Push elements
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after push:", stack)

# Pop element
stack.pop()
print("Stack after pop:", stack)

# Peek (top element)
print("Top element:", stack[-1])
