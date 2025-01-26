
def solutions(array):
    
    res = [0] * (max(array) + 1)
    
    print(min(array) )
    
    for i in array:
        if i in array:
            res[i] += 1
    for i in range(len(res)):
 
        print(f"Value = {i} || Number = {res[i]} ")
    


a = [2, 4, 3, 6, 1, 2, 8, 4, 2, 1]


solutions(a)


