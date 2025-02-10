class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert a new node
    def insert(self, root, key):
        # If the tree is empty, return a new node
        if root is None:
            return Node(key)

        # Otherwise, recur down the tree
        if key < root.value:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        return root

    # A wrapper function for insert
    def insert_key(self, key):
        self.root = self.insert(self.root, key)

    # Search for a node
    def search(self, root, key):
        # Base case: root is null or key is present at the root
        if root is None or root.value == key:
            return root

        # Key is greater than the root's value
        if key > root.value:
            return self.search(root.right, key)

        # Key is smaller than the root's value
        return self.search(root.left, key)

    # A wrapper function for search
    def search_key(self, key):
        result = self.search(self.root, key)
        return result is not None

    # Inorder Traversal (Left, Root, Right)
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.value, end=" ")
            self.inorder(root.right)

    # Preorder Traversal (Root, Left, Right)
    def preorder(self, root):
        if root:
            print(root.value, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # Postorder Traversal (Left, Right, Root)
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.value, end=" ")

    # Delete a node
    def delete(self, root, key):
        # Base case: If the tree is empty
        if root is None:
            return root

        # If the key to be deleted is smaller than the root's key, then it lies in the left subtree
        if key < root.value:
            root.left = self.delete(root.left, key)

        # If the key to be deleted is greater than the root's key, then it lies in the right subtree
        elif key > root.value:
            root.right = self.delete(root.right, key)

        # If the key is the same as the root's key, then this is the node to be deleted
        else:
            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            temp = self.min_value_node(root.right)

            # Copy the inorder successor's content to this node
            root.value = temp.value

            # Delete the inorder successor
            root.right = self.delete(root.right, temp.value)

        return root

    # A wrapper function for delete
    def delete_key(self, key):
        self.root = self.delete(self.root, key)

    # Find the node with the minimum value
    def min_value_node(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

# Example usage
bst = BinarySearchTree()
bst.insert_key(20)
bst.insert_key(8)
bst.insert_key(22)
bst.insert_key(4)
bst.insert_key(12)
bst.insert_key(10)
bst.insert_key(14)

print("Inorder Traversal (Ascending order):")
bst.inorder(bst.root)  # Output: 4 8 10 12 14 20 22

print("\nPreorder Traversal:")
bst.preorder(bst.root)  # Output: 20 8 4 12 10 14 22

print("\nPostorder Traversal:")
bst.postorder(bst.root)  # Output: 4 10 14 12 8 22 20

# Search for a key
print("\nSearching for key 10:")
print("Found" if bst.search_key(10) else "Not Found")  # Output: Found

# Delete a node
bst.delete_key(20)
print("\nInorder Traversal after deletion of 20:")
bst.inorder(bst.root)  # Output: 4 8 10 12 14 22
