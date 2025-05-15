class Stack:
    def __init__(self, items=None):
        if items is None:
            self.items = []
        else:
            self.items = items

    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop() if not self.is_empty() else -1

    def peek(self):
        return self.items[-1] if not self.is_empty() else -1
    
    def is_empty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def __str__(self) -> str:
        s = f"Stack of {str(self.size())} items: "
        for element in self.items:
            s += f"{str(element)} "
        return s


def evaluate_postfix(expression):
    stack = Stack()
    
    for char in expression:
        if char.isdigit():
            # Push operand to stack (convert char to int)
            stack.push(int(char))
        else:
            # Pop the top two elements from the stack
            right = stack.pop()
            left = stack.pop()
            
            # Apply the operator and push the result back to stack
            if char == '+':
                stack.push(left + right)
            elif char == '-':
                stack.push(left - right)
            elif char == '*':
                stack.push(left * right)
            elif char == '/':
                stack.push(left / right)
    
    # The final result should be the only element in the stack
    return stack.pop()

# Example usage
postfix_expr = "3528-*89+"
result = evaluate_postfix(postfix_expr)
print("Result of postfix expression:", result)
