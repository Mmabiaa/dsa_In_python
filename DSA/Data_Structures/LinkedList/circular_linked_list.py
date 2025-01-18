class CircularNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = CircularNode(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head  # Pointing to itself (circular)
            return
        
        last = self.head
        while last.next != self.head:
            last = last.next
        
        last.next = new_node
        new_node.next = self.head

    def display(self):
        if not self.head:
            return "List is empty."
        
        result = []
        current = self.head
        while True:
            result.append(current.data)
            current = current.next
            if current == self.head:
                break
        
        return " -> ".join(map(str, result))

# Example usage
if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.append(1)
    cll.append(2)
    cll.append(3)
    print("Circular Linked List:")
    print(cll.display())
