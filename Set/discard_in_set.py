store = set((1, 3, 2, 7, 10))

store.remove(1)
print(store)
print()


store.discard(10) # why because if i give "store.remove(10)" it shows error
print(store)
print()

store.remove(7)
print(store)