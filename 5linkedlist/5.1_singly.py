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