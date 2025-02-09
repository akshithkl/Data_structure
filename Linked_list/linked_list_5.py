# 3. Traversal in Linked List

class Node:
    def __init__(self, data):
        self.data = data  # Example: n1 = Node(20), n2 = Node(30)...
        self.next = None  # Initially, next is None

class sinly_link:
    def __init__(self):
        self.head = None  # Initialize empty linked list
    
    def traversal(self):
        if self.head is None:
            print("Singly linked list is empty")
        else:
            a = self.head
            while a is not None:
                print(a.data, end=" -> " if a.next else "")  # Print arrow only if next node exists
                a = a.next
            print()  # New line after traversal

    # 4. Insertion at the Beginning
    def insert_at_beginning(self, data):
        print()
        nb = Node(data)
        nb.next = self.head
        self.head = nb 

    # 5. Insertion at the End
    def insert_at_end(self, data):
        print()
        ne = Node(data)
        if self.head is None:
            self.head = ne
            return
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = ne 

    # 6. Insertion at a Specified Position
    def insert_at_specified_node(self, position, data):
        print()
        nib = Node(data)
        a = self.head
        for i in range(1, position - 1):
            if a is None:
                print("Position out of range")
                return
            a = a.next
        nib.next = a.next
        a.next = nib

    # 7. Deletion at the Beginning
    def deletion_at_beginning(self):
        print()
        if self.head is None:
            print("List is empty")
            return
        a = self.head
        self.head = a.next 
        a.next = None

    # 8. Deletion at the End
    def deletion_at_end(self):
        print()
        if self.head is None:
            print("List is empty")
            return
        prev = self.head
        a = self.head.next
        if a is None:  # If only one node exists
            self.head = None
            return
        while a.next is not None:
            a = a.next
            prev = prev.next
        prev.next = None

    # 9. Deletion at a Specified Position
    def deletion_at_particular_node(self, position):
        print()
        if self.head is None:
            print("List is empty")
            return
        prev = self.head
        a = self.head.next
        for i in range(1, position - 1):
            if a is None:
                print("Position out of range")
                return
            a = a.next
            prev = prev.next
        prev.next = a.next
        a.next = None

# Create Linked List
sll = sinly_link()              

n1 = Node(20)
n2 = Node(30)
sll.head = n1 
n1.next = n2 

n3 = Node(40)
n2.next = n3

n4 = Node(60)       
n3.next = n4        

sll.traversal()  # Output: 20 -> 30 -> 40 -> 60

sll.insert_at_beginning(2)
sll.traversal()  # Output: 2 -> 20 -> 30 -> 40 -> 60

sll.insert_at_end(500)
sll.traversal()  # Output: 2 -> 20 -> 30 -> 40 -> 60 -> 500

sll.insert_at_specified_node(3, 77)
sll.traversal()  # Output: 2 -> 20 -> 77 -> 30 -> 40 -> 60 -> 500

sll.deletion_at_beginning()
sll.traversal()  # Output: 20 -> 77 -> 30 -> 40 -> 60 -> 500

sll.deletion_at_end()
sll.traversal()  # Output: 20 -> 77 -> 30 -> 40 -> 60

sll.deletion_at_particular_node(3)
sll.traversal()  # Output: 20 -> 77 -> 40 -> 60
