from collections import deque
q = deque()  # Create a deque object
q.append(51)
q.append(32)
q.append(7)
q.append(5)
q.append(6)

q.pop()  # Removes the last element

print(q)        # Shows the deque after pop
print(q.pop())  # Prints the removed element (which is 6)


#output
#deque([51, 32, 7, 5])
#5
