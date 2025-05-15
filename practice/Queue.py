class Queue():
    def __init__(self, ls = None):
        self.queue = []

    def size(self):
        return len(self.queue)

    def isEmpty(self):
        return True if self.size() == 0 else False

    def enQueue(self, val):
        self.queue.append(val)

    def deQueue(self):
        return self.queue.pop(0)

    def __str__(self):
        s = f"queue of {str(self.size())} items : "
        for element in self.queue :
            s += f"{str(element)} "
        return s
    
f = [7,5,8,0,3,2,5,3,34,46]
queue = Queue()
for num in f:
    queue.enQueue(num)

print(queue)