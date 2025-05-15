parent = list(str(input("Enter Input : ")))
open_list = ["[","{","("]
close_list = ["]","}",")"]
stack = []
missing_count =0
for i in parent:
    if i in open_list:
        stack.append(i)
    elif i in close_list:
        pos = close_list.index(i)
        if len(stack) > 0 and open_list[pos] == stack[-1]:
            stack.pop()
        else:
            missing_count += 1
            
missing_count += len(stack)
print(missing_count)
if missing_count == 0 :
    print("Perfect ! ! !")