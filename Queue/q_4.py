from collections import deque

my_list = deque([1, 2, 3])
my_list.appendleft(41)  # Adds 41 to the beginning of the deque
print(list(my_list))    # Convert deque back to a list for display (optional)
