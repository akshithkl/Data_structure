a ={54, 34, 8, 9}
b = [3, 7, 9, 4, 2]
k = (2, 4, 8, 1)

c = a.union(b)   # "|" this symbol shows error , because "b" is a list then union coverted into set
print()
print("............Using tuple.............")
print(c)

d = a.intersection(b)
print(d)
print()

print("............Using tuple.............")
m = a.union(k)# | this symbol shows error , because "m" is a list then union coverted into set

print(m)

h = a.intersection(k)
print(h)
print()