class Stack :
    def __init__(self , list = None):
        if list == None :
            self.items = []
        else :
            self.items = list
    def __str__(self) -> str:
        s = f"stack of {str(self.size())} items :"
        for element in self.items :
            s += f"{str(element)} "
        return s
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        try :
           return self.items[-1]
        except :
            return -1
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)


s1 = Stack()
mushroom = 0

list_opt = input("Enter Input : ").split(",")
for opt in list_opt:
    action =  opt.split(" ")
    if action[0]== "A":
        s1.push(int(action[1]))
    elif action[0]== "B":
        s2 = Stack()
        temp = Stack()
        if s1.peek() != -1 :
            temp.push(s1.peek())
            s2.push(s1.pop())
            for i in range(s1.size()):
                temp.push(s1.peek())
                if s2.peek() < s1.peek() :
                    s2.push(s1.pop())
                else :
                    s1.pop()
        print(s2.size())
        for i in range(temp.size()):
            s1.push(temp.pop())
    elif action[0]=="S":
        s2 = Stack()
        for i in range(s1.size()):
            if s1.peek() != -1 :
                if s1.peek() % 2 != 0 :
                    s2.push(s1.pop()+2)
                else :
                    s2.push(s1.pop()-1)
        for i in range(s2.size()):
            s1.push(s2.pop())