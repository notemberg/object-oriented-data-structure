class Stack:
    def __init__(self , list = None):
        if list == None :
            self.items = []
        else :
            self.items = list

    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop() if not self.is_empty() else -1

    def peek(self):
        return self.items[-1] if not self.is_empty() else -1
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def __str__(self) -> str:
        s = f"stack of {str(self.size())} items : "
        for element in self.items :
            s += f"{str(element)} "
        return s

s = [7,5,8,0,3,2,5,3,34,46]
stack = Stack()
for num in s:
    stack.push(num)

print(stack)

