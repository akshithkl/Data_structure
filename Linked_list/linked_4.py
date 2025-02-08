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


# 4. insertion
    
    def insert_at_beginning(self, data):
        print()  
        nb = Node(data)  # object
        nb.next = self.head
        self.head = nb 
# 5. insertion at end
    def insert_at_end(self, data):
        print()
        ne = Node(data)
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = ne 
        
# 6. insertion in between
    
    def insert_at_specified_node(self, position, data):
        print()
        nib = Node(data)
        a = self.head
        for i in range(1, position - 1):
            a = a.next
        nib.next = a.next
        a.next = nib
        
# 7.Deletion at beginning
    
    def deletion_at_beginning(self):
        print()
        a = self.head 
        self.head = a.next 
        a.next = None

# 8. Deletion at end
    def deletion_at_end(self):
        print()
        prev = self.head
        a = self.head.next
        while a.next is not None:
            a = a.next
            prev = prev.next
        prev.next = None

# 9. Deletion at specified node
    
    def deletion_at_particular_node(self, position):
        print()
        prev = self.head
        a = self.head.next
        for i in range(1, position - 1):
            a = a.next
            prev = prev.next
        prev.next = a.next
        a.next = None
        
        
 
 
sll = sinly_link()              
              
n1 = Node(20)
n2 = Node(30)
sll.head = n1 
n1.next = n2 

n3 =Node(40)
n2.next = n3

n4 = Node(60)       
n3.next = n4        

sll.traversal()

sll.insert_at_beginning(2)
sll.traversal()

sll.insert_at_end(500)
sll.traversal()



sll.insert_at_specified_node(3, 77)
sll.traversal()


sll.deletion_at_beginning()
sll.traversal()


sll.deletion_at_end()
sll.traversal()

sll.deletion_at_particular_node(3)
sll.traversal()
