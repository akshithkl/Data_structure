# Balanced Binary Tree (Height Balanced)

def is_balanced(root):
    def check(root):
        if not root: return 0, True
        lh, is_left_bal = check(root.left)
        rh, is_right_bal = check(root.right)
        is_bal = abs(lh - rh) <= 1 and is_left_bal and is_right_bal
        return max(lh, rh) + 1, is_bal
    return check(root)[1]


# Time Complexity: O(n)
# Space Complexity: O(h)
