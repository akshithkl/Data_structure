s = "ABCDEFG"
a = {}

m = 1
for char in s:
    a[char] = a.get(char, 0) + m  # Initialize missing keys with 0 and increment
    m += 1

print(a)
