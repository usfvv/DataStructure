class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None
    
    def insert_first(self, val):
        new_node = Node(val)
        if self.is_empty():
            self.head = self.tail = new_node
        else :
            new_node.next = self.head
            self.head = new_node

    def insert_last(self, val):
        new_node = Node(val)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def insert_at_position(self, val, position):
        new_node = Node(val)
        if position < 0 or self.is_empty():
            self.insert_first(val)
            return 
        current = self.head
        count = 0
        while current.next and count < position - 1:
            current = current.next
            count += 1
        new_node.next = current.next
        current.next = new_node
        if new_node.next is None:
            self.tail = new_node

    def remove_first(self):
        if self.is_empty():
            print("List is empty")
            return
        print(f"Removing first {self.head.data}")
        self.head = self.head.next
        if self.head is None:
            self.tail = None

    def remove_last(self):
        if self.is_empty():
            print("List is empty")
            return
        if self.head.next is None :
            print(f"Removing last :{self.head.data}") 
            self.head = self.tail = None
            return
        current = self.head
        while current.next != self.tail:
            current = current.next
        print(f"Removing last : {self.tail.data}")
        current.next = None
        self.tail = current

    def remove_key(self, val):
        if self.is_empty():
            print("List is empty")
            return
        current = self.head
        prev = None
        while current:
            if current.data == val :
                if prev is None:
                    print(f"Removing head with key {val}")
                    self.head = current.next
                    if self.head is None :
                        self.tail = None
                else:
                    print(f"Removing key {val}")
                    prev.next = current.next
                    if current == self.tail:
                        self.tail = prev
                return
            prev = current
            current = current.next
        print(f"value {val} not found.")

    def reverse(self):
        if self.is_empty() or self.head.next is None :
            return
        prev = None
        current = self.head
        self.tail = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev

    def search(self, element):
        if self.is_empty():
            print("List is empty")
        current = self.head
        pos = 0
        while current is not None:
            if current.data == element:
                return f"Element {current.data} in index -> {pos}"
            current = current.next
            pos += 1
        return "Element not found"

    def display(self):
        if self.is_empty():
            print("List is empty")
            return 
        current = self.head
        print("Linked list: ", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


ll = SinglyLinkedList()
ll.insert_last(1)
ll.insert_last(2)
ll.insert_last(3)
ll.insert_last(4)

ll.display()          # 1 -> 2 -> 3 -> 4 -> None
ll.reverse()
ll.display()          # 4 -> 3 -> 2 -> 1 -> None

print(ll.search(3))   #Element 3 in index -> 1