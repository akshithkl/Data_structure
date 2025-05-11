def solution(num, arr = []):
    
    print(arr)
    
    for i in num:
        if i not in arr:
            solution( num, arr + [i])
        
    # print(arr)

num = [1, 2, 3]
solution(num)