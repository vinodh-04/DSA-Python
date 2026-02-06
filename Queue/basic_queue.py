# Basic Queue implementation using Python list

queue = []

# Enqueue (add elements)
queue.append(10)
queue.append(20)
queue.append(30)

print("Queue after enqueue:", queue)

# Dequeue (remove first element)
queue.pop(0)
print("Queue after dequeue:", queue)

# Peek (front element)
print("Front element:", queue[0])
