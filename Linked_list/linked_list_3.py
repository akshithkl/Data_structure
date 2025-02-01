# 3. Traversal in Linked list

class Node:
    def __init__(self, data):
        self.data = data      # n1 = data = 20, n2.data = 30.....
        self.next = None      # n1.next = None, n2.next = None....

class sinly_link:
    def __init__(self):
        self.head = None  # sll.head = None
    
    def traversal(self):
        if self.head is None:
            print("singly linked list is empty ")
        
        else:
            a = self.head     # a = sll.head 
            while a is not None: # a = sll.head 
                print(a.data, end=" ")   # a.data = n1.data   
                a = a.next               # a =n1.next --> [ "n2" ] , a = n2.next,..., a = n4.next -->["None"]
               
 
sll = sinly_link()              
              
n1 = Node(20)
n2 = Node(30)
sll.head = n1 
n1.next = n2 

n3 = Node(40)
n2.next = n3

n4 = Node(60)       
n3.next = n4        

sll.traversal()
