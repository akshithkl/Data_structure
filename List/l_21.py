a = [2, 4, 3, 6, 1, 2, 8, 4, 2, 1]
print(a.index(4))

#  a.index(value, start)

print(a.index(2, 3))  # Starts searching from index 3 → Output: 5


# a[3] = 6
# a[4] = 1
# a[5] = 2 ← this is the first `2` found starting from index 3
# So, it returns 5 because that’s the index of the 2 it found.


# So why exactly 2, 3?
# 2 is the value you are searching for.

# 3 is the index to start searching from.

# You're not searching for "2 at index 3" — you're saying:

# "Search for 2 starting from index 3, and return the first place you find it."

# In your list:

# python
# Copy
# Edit
# a = [2, 4, 3, 6, 1, 2, 8, 4, 2, 1]
#            ↑  ↑  ↑
# index:     0  1  2  3  4  5  6  7  8  9