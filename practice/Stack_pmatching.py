class Stack:
    def __init__(self, list=None):
        if list is None:
            self.items = []
        else:
            self.items = list

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if not self.isEmpty() else -1

    def peek(self):
        return self.items[-1] if not self.isEmpty() else -1

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def __str__(self) -> str:
        s = f"stack of {str(self.size())} items : "
        for element in self.items:
            s += f"{str(element)} "
        return s

def is_balanced_parentheses(expression):
    stack = Stack()
    opening = "({["
    closing = ")}]"
    
    for char in expression:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack.isEmpty():
                return False
            top = stack.pop()
            if char == ')' and top != '(':
                return False
            elif char == '}' and top != '{':
                return False
            elif char == ']' and top != '[':
                return False
    
    return stack.isEmpty()

# Testing the Stack class
s = [7, 5, 8, 0, 3, 2, 5, 3, 34, 46]
stack = Stack()
for num in s:
    stack.push(num)

print(stack)

# Testing the parentheses matching function
expression1 = "{[()()]}"
expression2 = "{[(])}"
print(f"Is the expression '{expression1}' balanced? {is_balanced_parentheses(expression1)}")
print(f"Is the expression '{expression2}' balanced? {is_balanced_parentheses(expression2)}")
