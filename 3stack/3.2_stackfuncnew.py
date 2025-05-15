
class Stack:
  def __init__(self):
    self.stack = []

  def pop(self):
    return self.stack.pop() if not self.is_empty() else -1

  def push(self, item):
    self.stack.append(item)

  def peek(self):
    return self.stack[-1] if not self.is_empty() else -1

  def is_empty(self):
    return self.stack == []

  def size(self):
    return len(self.stack)


def ManageStack(commands):
  stack = Stack()
  temp_stack = Stack()
  
  for command in commands:  
    if command[0] == 'A':
      stack.push(int(command[1]))
      print(f'Add = {int(command[1])}')
      
    elif command[0] == 'P':
      if stack.is_empty():
        print(-1)
      else:
        print(f'Pop = {stack.pop()}')
              
    elif command[0] == 'D':
      if stack.is_empty():
        print(-1)
      else:
        while not stack.is_empty():
          pop_item = stack.pop()
          if pop_item != int(command[1]):
            temp_stack.push(pop_item) 
          else:
            print(f'Delete = {pop_item}')
            
    elif command[0] == 'LD':
      if stack.is_empty():
        print(-1)
      else:
        while not stack.is_empty():
          pop_item = stack.pop()
          if pop_item >= int(command[1]):
            temp_stack.push(pop_item) 
          else:
            print(f'Delete = {pop_item} Because {pop_item} is less than {command[1]}')
            
    elif command[0] == 'MD':
      if stack.is_empty():
        print(-1)
      else:
        while not stack.is_empty():
          pop_item = stack.pop()
          if pop_item <= int(command[1]):
            temp_stack.push(pop_item)
          else:
            print(f'Delete = {pop_item} Because {pop_item} is more than {command[1]}')
        
    while not temp_stack.is_empty():
      stack.push(temp_stack.pop())
    
  print(f"Value in Stack = {stack.stack}")



if __name__ == '__main__':
  commands = [i.split() for i in input('Enter Input : ').split(',')]
  
  ManageStack(commands)
  
