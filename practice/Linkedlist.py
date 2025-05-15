
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class LinkedList:
    def __init__(self,data = None):
        self.size = 0
        self.head = Node(None)
        if data != None:
            for i in data:
                self.append(i)

    def __str__(self):
        i = 0
        result = 'link list : '
        p = self.head
        while p != None:
                if self.size == 0:
                    result = 'List is empty'
                elif p.data != None:
                    result += str(p.data)
                    if i < self.whatSize():
                        result += '->'
                p = p.next
                i += 1
        return result

    def isEmpty(self):
        return self.size == 0
    
    def whatSize(self):
        return self.size
        
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
        else:
            last = self.head
            while last.next != None:
                last = last.next
            last.next = new_node
        self.size +=1

    def insert(self, index, data):
        temp=0
        if index >= 0 and index <= self.size:
            new_node = Node(data)
            print(f'index = {index} and data = {data}')
            if self.head == None:
                self.head = new_node
            else:
                last = self.head
                while temp < index:
                    last = last.next
                    temp += 1
                new_node.next = last.next
                last.next = new_node
                self.size += 1
        else:
            return print('Data cannot be added')    
        
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
        
inp = input('Enter Input : ').split(',')
lst_front = inp[0].split()
lst_add = []
for i in inp[1:]:
    lst_add.extend(i.split(':'))
    
c = LinkedList(lst_front)
print(c)
for i in range(len(lst_add)):
    if i % 2 == 0:
        c.insert(int(lst_add[i]),int(lst_add[i+1]))
        print(c)

# Enter Input : 0 1 2 4, 3:3
# link list : 0->1->2->4
# index = 3 and data = 3
# link list : 0->1->2->3->4

# Enter Input : 0 1 2 4, -1:2, 3:3, 5:5, 0:-1
# link list : 0->1->2->4
# Data cannot be added
# link list : 0->1->2->4
# index = 3 and data = 3
# link list : 0->1->2->3->4
# index = 5 and data = 5
# link list : 0->1->2->3->4->5
# index = 0 and data = -1
# link list : -1->0->1->2->3->4->5