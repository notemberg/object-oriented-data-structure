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

print(' ***Infix to Postfix***')
inp = input('Enter Infix expression : ')

S = Stack()

print('PostFix : ')

### Enter Your Code Here ###

operator = {
    "(" : 0,
    "+" : 1,
    "-" : 1,
    "/" : 2,
    "*" : 2,
    "^" : 3,
}


for i in range(len(inp)):
    
    opt = inp[i]
    if opt not in operator and opt != ")" :
        print(opt, end='')
    else :
        if opt == "(" :
            S.push(opt)
        elif opt == ")" :
            while S.peek() != "(" :
                if S.peek() != -1 :
                    print(S.pop(), end='')
                else :
                    break
            if S.peek() == "(":
                S.pop()
        elif S.peek() not in operator :
            S.push(opt)
        else :
            if S.peek() != -1 :
                if operator[S.peek()] < operator[opt] :
                    S.push(opt)
                elif operator[S.peek()] == operator[opt] :
                    print(S.pop(), end='')
                    S.push(opt)
                else :
                    for i in range(S.size()):
                        if S.peek() == "(" :
                            break
                        print(S.pop(), end='')
                    S.push(opt)


for i in range(S.size()) :
    print(S.pop(), end='')
print()