from bintrees import RBTree

tree = RBTree()
tree.insert(10, "a")
tree.insert(20, "b")
tree.insert(15, "c")
print(list(tree.items()))  # Output: [(10, 'a'), (15, 'c'), (20, 'b')]


# Time Complexity: O(log n) for insert/search/delete
# Space Complexity: O(n)