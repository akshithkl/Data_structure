
def d(k):
        
    dict_list = {}


    for key in k:
        if key in  dict_list:
            dict_list[key] += 1
        else:
            dict_list[key] = 1 
    print("Character count:", dict_list)
    
   
    for key, value in dict_list.items():
        if value > 1:
            
            print("\n Highest elements")
            print(f"key = {key} : value = {value}") 



k = input("Enter the words : ")

f = d(k)

