
queue = []

queue.insert(0,1)
queue.insert(0,2)
queue.insert(0,12)
queue.insert(0,31)
queue.insert(0,14)

print(queue)

print("----------")
queue.pop()

print(queue)

#output
#           [14, 31, 12, 2, 1]
#           ----------
#           [14, 31, 12, 2]
