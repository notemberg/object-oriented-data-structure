class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next  
            current.next = prev       
            prev = current           
            current = next_node       
        self.head = prev               

    def __str__(self):
        result = "Linked List: "
        temp = self.head
        while temp:
            result += str(temp.data) + " -> "
            temp = temp.next
        return result.strip(" -> ")

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
print("Before reversing:")
print(ll)

ll.reverse()
print("After reversing:")
print(ll)
