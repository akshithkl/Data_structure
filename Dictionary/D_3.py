def d(k):
        
    dict_list = {}


    count = 0
    for h in k:
        if h in  dict_list:
            count += 1
        else:
            dict_list[h] = 1 
    print(count)


f = d('akshithhhh')

