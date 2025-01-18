import collections

queue = collections.deque()  # Initialize a deque

# Add tuples to the queue
queue.append((1, 3, 4))  # Append a tuple with three values
queue.append((2, 5, -1))

# Process the queue
while queue:
    item = queue.popleft()  # Pop the first element
    moves, position, speed  = item  # Unpack the tuple
    print(f"Moves: {moves}, Position: {position}, Speed: {speed}")
