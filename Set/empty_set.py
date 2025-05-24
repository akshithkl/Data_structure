s = set()
s.add(3) # if you add the element use add , append not work
s.add(6)
s.add(1)
s.add(4)
s.add(2)
print(f'.1: {s}')
print()

s.pop()
print(f'.2: {s}')
print()

s.add(10)
print(f'.3: {s}')
print()

s.update([11, 25, 33])  # Add multiple elements to the set
print(f'.3: {s}')
print()

s.update(["hello"])
print(f'.4: {s}')
print()

s.update(("ORDER"))
print(f'.4: {s}')
print()

s.add(("everyone"))
print(f'.5: {s}')
print()

s.add("little")
print(f'.6: {s}')


s.update([50, 60, 70, 80, 90])  
print(f'.7: {s}')
print()