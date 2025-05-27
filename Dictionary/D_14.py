dictionary = {2: 3, 4: 2, 3: 1, 6: 1, 1: 2, 8: 1}
d = sorted(dictionary)

for key, value in sorted(dictionary.items()):
    print(f"Value = {key} || Number = {value}")
    
print(d)
