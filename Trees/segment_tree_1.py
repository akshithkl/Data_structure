class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, idx, l, r):
        if l == r:
            self.tree[idx] = arr[l]
        else:
            mid = (l + r) // 2
            self.build(arr, 2 * idx + 1, l, mid)
            self.build(arr, 2 * idx + 2, mid + 1, r)
            self.tree[idx] = self.tree[2 * idx + 1] + self.tree[2 * idx + 2]

    def query(self, idx, l, r, ql, qr):
        if qr < l or ql > r: return 0
        if ql <= l and r <= qr: return self.tree[idx]
        mid = (l + r) // 2
        return self.query(2 * idx + 1, l, mid, ql, qr) + self.query(2 * idx + 2, mid + 1, r, ql, qr)

# Input
arr = [1, 3, 5, 7, 9, 11]
st = SegmentTree(arr)
print(st.query(0, 0, len(arr)-1, 1, 3))  # Output: 15


# Time Complexity:

# Build: O(n)

# Query: O(log n)

# Update (not shown): O(log n)

# Space Complexity: O(4n)