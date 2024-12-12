class Node:
    def __init__(self, data):
        self.data = data  # Initialize node with data
        self.next = None  # Next pointer initialized to None

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize head of the linked list to None

    # Method to insert a new node at the end of the list (optional)
    def append(self, data):
        new_node = Node(data)  # Create a new node
        if not self.head:  # If list is empty, make new node the head
            self.head = new_node
            return
        
        last = self.head  # Start from head and traverse to the end
        while last.next:
            last = last.next
        
        last.next = new_node  # Link new node at the end of the list
