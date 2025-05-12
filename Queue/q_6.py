class MyQueue:
    def __init__(self):
        self.queue = []  # Initialize an empty list as a queue

    def enqueue(self, x: int) -> None:
        """Insert an element at the back of the queue."""
        self.queue.append(x)

    def dequeue(self) -> int:
        """Remove and return the front element of the queue. Return -1 if empty."""
        if self.is_empty():
            return -1
        return self.queue.pop(0)

    def front(self) -> int:
        """Get the front element of the queue. Return -1 if empty."""
        if self.is_empty():
            return -1
        return self.queue[0]

    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def size(self) -> int:
        """Return the number of elements in the queue."""
        return len(self.queue)
    
    
q = MyQueue()
q.enqueue(10)
q.enqueue(20)
print(q.front())   # Output: 10
print(q.dequeue()) # Output: 10
print(q.is_empty())# Output: False
print(q.size())    # Output: 1
print(q.dequeue()) # Output: 20
print(q.dequeue()) # Output: -1 (Queue is empty)
