x = (input("Enter Input : ")).split(",")

def ManageStack(string):
    stack,temp =[],[]
    for i in string :
        parts = i.split(' ')
        num = int(parts[1]) if len(parts) > 1 else int(parts[0])

        if 'P' in i :
            if len(stack) == 0 : 
                print('-1')
            else : 
                print(f"Pop = {stack[-1]}")
                stack.pop()

        elif 'A' in i :
            stack.append(num)
            print(f"Add = {num}")

        elif 'M' in i :
            if len(stack) == 0 : print('-1')
            else:
                temp=stack
                for j in stack :
                    if int (j) > int(num):
                        temp.remove(j)
                print(f'Delete = {j} Because {j} is more than {num}')         
                stack=temp
    
        elif 'L' in i :    
            if len(stack) == 0 : print('-1') 
            else:
                temp=stack
                for j in stack :
                    if  int(j) < int(num):
                        temp.remove(j)
                stack=temp
                print(f'Delete = {j} Because {j} is less than {num}')

        elif 'D'in i :
            if len(stack) == 0 : print('-1')
            else:
                temp = stack[:]
                print(temp)
                for j in stack:
                    if int(j) == int(num):
                        temp.remove(j)
                print(f'Delete = {j}')
                stack = temp
    return stack

print(f"Value in Stack = {ManageStack(x)}")

# A 3,A 3,A 3,P,A 2,A 10,A 5,A 7,A 8,D 3,LD 5