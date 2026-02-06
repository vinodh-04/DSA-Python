# Queue operations using list

queue = []

def enqueue(item):
    queue.append(item)
    print("Enqueued:", item)

def dequeue():
    if not queue:
        print("Queue is empty")
    else:
        print("Dequeued:", queue.pop(0))

def peek():
    if not queue:
        print("Queue is empty")
    else:
        print("Front element:", queue[0])

# Testing
enqueue(5)
enqueue(10)
peek()
dequeue()
peek()
