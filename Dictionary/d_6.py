def solutions(array):
    res = {}

    for i in array:
        
        if i in res:
            res[i] += 1
        else:
            res[i] = 1
    
    for key, value in sorted(res.items()):
        print(f"Value = {key} || Number = {value}")

a = [2, 4, 3, 6, 1, 2, 8, 4, 2, 1]

solutions(a)
