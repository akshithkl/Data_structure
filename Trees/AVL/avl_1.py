# AVL Tree (Self-balancing BST)

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None
        self.height = 1

def get_height(root):
    return root.height if root else 0

def get_balance(root):
    return get_height(root.left) - get_height(root.right) if root else 0

def right_rotate(z):
    y = z.left
    T3 = y.right
    y.right = z
    z.left = T3
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y

def left_rotate(z):
    y = z.right
    T2 = y.left
    y.left = z
    z.right = T2
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y

def insert(root, key):
    if not root: return AVLNode(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)

    if balance > 1 and key < root.left.key:
        return right_rotate(root)
    if balance < -1 and key > root.right.key:
        return left_rotate(root)
    if balance > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if balance < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)
    
    return root

# Input
root = None
for k in [10, 20, 30]:
    root = insert(root, k)


# Time Complexity: O(log n)
# Space Complexity: O(log n)
