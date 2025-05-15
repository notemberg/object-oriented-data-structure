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

    def remove_duplicates(self):
        if self.head is None:
            return

        current = self.head
        seen = set()
        prev = None

        while current:
            if current.data in seen:
                prev.next = current.next 
            else:
                seen.add(current.data)
                prev = current
            current = current.next

    def __str__(self):
        result = "Linked List: "
        temp = self.head
        while temp:
            result += str(temp.data) + " -> "
            temp = temp.next
        return result.strip(" -> ")

# Example usage:
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(2)
ll.append(4)
ll.append(3)
print("Before removing duplicates:")
print(ll)

ll.remove_duplicates()
print("After removing duplicates:")
print(ll)
