class Queue:
    def __init__(self , items=None):
        if items :
            self.items = items
        else :
            self.items = []
    def enQueue(self,item):
        self.items.append(item)
        return item
    def deQueue(self):
        if self.isEmpty():
            return -1
        return self.items.pop(0)
    def isEmpty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)



q1 = Queue()

left,right =  input("Enter Input : ").split("/")

employee = {}

def getKey(department_id):
    for key in employee.keys() :
            if department_id in employee[key] :
                department = key
    return department


for condition in left.split(",") :
    department , department_id =  condition.split(" ")
    try :
        employee[department].append(department_id)
    except :
        employee[department] = [department_id]

for condition in right.split(",") :
    try :
        opt , department_id =  condition.split(" ")
    except :
        opt = condition
    if opt == "D" :
        # print(q1.items)
        check = q1.deQueue()
        if check == -1 :
            print("Empty")
        else :
            print(check)
    elif opt == "E" :
        if q1.isEmpty() :
            q1.enQueue(department_id)
            continue
        department = getKey(department_id)
        q2 = Queue()
        check = False
        ok = False
        for i  in range(q1.size()):
            department_id_q1 = q1.deQueue() 
            department_q1 = getKey(department_id_q1) 
            if department != department_q1:
                if check :
                    q2.enQueue(department_id)
                    check = False
                    ok = True
                q2.enQueue(department_id_q1)
            elif department == department_q1 :
                q2.enQueue(department_id_q1)
                check = True
        else :
            if not ok :
                q2.enQueue(department_id)
        
        for i in range(q1.size()):
            q2.enQueue(q1.deQueue())

        for i in range(q2.size()):
            q1.enQueue(q2.deQueue())