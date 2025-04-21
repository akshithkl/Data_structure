class NaryNode:
    def __init__(self, val):
        self.val = val
        self.children = []

def print_tree(root):
    if root:
        print(root.val, end=" ")
        for child in root.children:
            print_tree(child)

# Input
root = NaryNode(1)
root.children.append(NaryNode(2))
root.children.append(NaryNode(3))
root.children[1].children.append(NaryNode(4))
print_tree(root)  # Output: 1 2 3 4


# Time Complexity: O(n)
# Space Complexity: O(h)