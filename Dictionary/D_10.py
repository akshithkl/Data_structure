from collections import Counter
nam ='akshith'
my_dict = Counter()

for i, v in enumerate(nam):
  
    my_dict[v] += 1

    
        

my_dict['a'] -= 1

print(my_dict)

'''
Why no KeyError?
Counter is a subclass of dict, but it automatically initializes missing keys to 0 when you increment them.
When window_counter[c] += 1 runs for the first time, Counter sees that c is not in the dictionary and assumes window_counter[c] = 0, then increments it to 1.
This built-in behavior prevents a KeyError.

'''
