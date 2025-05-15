class Node:
    def __init__(self,x):
        self.data = x
        self.next = None

class LinkedList:
    def __init__(self,data=None) :
        self.size = 0
        self.head = Node(None)
        if data  != None:
            for i in data:
                self.append(i)

    def __str__(self):
        result = "Linked List: "
        temp = self.head
        while temp:
            result += str(temp.data) + " -> "
            temp = temp.next
        return result.strip(" -> ")

    def isEmpty(self):
        return self.size == 0
     
    def whatSize(self):
        return self.size

    def append(self,new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node

        else:
            last= self.head
            while last.next != None:
                last = last.next
            last.next = new_node
        self.size +=1

    def insert(self,index,data):
        temp=0 
        if index >= 0 and index <= self.size:
            new_node = Node(data)
            if self.head == None:
                self.head = new_node
            else:
                last= self.head
                while temp < index:
                    last = last.next
                    temp += 1
                new_node.next = last.next
                last.next = new_node
                self.size +=1

    def delete(self, index):
        if index < 0 or index >= self.size:
            print('Index out of range')
            return
        
        if self.head is None or self.head.data is None: 
            print('List is empty')
            return
        
        if index == 0:
            print(f'delete {self.head.data} at index {index}')
            self.head = self.head.next
        else:
            temp = 0
            current = self.head
            while temp < index - 1:
                current = current.next
                temp += 1
            print(f'delete {current.next.data} at index {index}')
            current.next = current.next.next
            self.size -= 1

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next  # Store the next node
            current.next = prev       # Reverse the link
            prev = current            # Move prev to this node
            current = next_node       # Move to the next node
        self.head = prev               # Update the head to the new first node

    def detectLoop(self):
        s = set()
        temp = self.head
        while (temp):
            if (temp in s):
                return True
            s.add(temp)
            temp = temp.next
        return False
    
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

    def set_next(self, idx1, idx2):
        if self.head is None:
            print("Error! {list is empty}")
            return
        
        node1 = self._get_node_at_index(idx1)
        if not node1:
            print(f"Error! {{index not in length}}: {indx1}")
            return
        
        node2 = self._get_node_at_index(idx2)
        if not node2:
            self.append(idx2)
            print(f"index not in length, append : {idx2}")
        else:
            node1.next = node2
            print(f"Set node.next complete!, index:value = {idx1}:{node1.data} -> {idx2}:{node2.data}")

    def _get_node_at_index(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                return current
            count += 1
            current = current.next
        return None