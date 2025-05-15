class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def printList(self):
        if self.head is None:
            print("Empty")
            return
        temp = self.head
        visited = set()
        nodes = []
        while temp:
            if temp in visited:
                break
            nodes.append(str(temp.data))
            visited.add(temp)
            temp = temp.next
        print("->".join(nodes))

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

    def detectLoop(self):
        s = set()
        temp = self.head
        while (temp):
            if (temp in s):
                return True
            s.add(temp)
            temp = temp.next
        return False
    
    def LoopStatus(self):
        if self.detectLoop():
            return True
        else:
            return False

llist = LinkedList()
execution = (input("Enter input : ")).split(",")
for command in execution:
    parts = command.split(' ')
    num = parts[1]
    letter = parts[0]
    if 'A' in letter.upper():
        llist.append(int(num))
        llist.printList()
    if 'S' in letter.upper():
        indx1,indx2 = map(int,num.split(":"))
        llist.set_next(indx1,indx2)

if llist.LoopStatus() ==True:
    print("Found Loop")
else:
    print("No Loop")
    llist.printList()

# Enter input : A 0,A 3,A 5,A 7,A 9,S 2:0
# 0
# 0->3
# 0->3->5
# 0->3->5->7
# 0->3->5->7->9
# Set node.next complete!, index:value = 2:5 -> 0:0
# Found Loop

# Enter input : S 0:0,A 0,A 0,A 0,S 0:5,S 0:3,A 5,S 2:1
# Error! {list is empty}
# 0
# 0->0
# 0->0->0
# index not in length, append : 5
# Set node.next complete!, index:value = 0:0 -> 3:5
# 0->5->5
# Set node.next complete!, index:value = 2:5 -> 1:5
# Found Loop
