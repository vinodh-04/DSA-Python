# Stack operations using list

stack = []

def push(item):
    stack.append(item)
    print("Pushed:", item)

def pop():
    if not stack:
        print("Stack is empty")
    else:
        print("Popped:", stack.pop())

def peek():
    if not stack:
        print("Stack is empty")
    else:
        print("Top element:", stack[-1])

# Testing
push(5)
push(10)
peek()
pop()
peek()
