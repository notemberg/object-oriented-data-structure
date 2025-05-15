class Queue :
    def __init__(self, items=None):
        if items :
            self.items = items
        else :
            self.items = []
    def deQueue(self):
        if self.isEmpty() :
            return -1
        return self.items.pop(0)
    def enQueue(self,item):
        self.items.append(item)
        return item
    def isEmpty(self):
        return len(self.items) == 0 
    def size(self):
        return len(self.items)
    def clear(self):
        self.items = []
    
q1 = Queue() # ทางที่เคยเดิน
q3 = Queue() # ทางที่เดินได้
width , height , room =  input("Enter width, height, and room: ").split(" ")
room  = room.split(",")
map_room = []
start = False
err =  False
exit_room = True
frist = False
width = int(width)
height = int(height)

move_ment = [(0,-1) , (1,0), (0,1) , (-1,0)]


for i in range(height):
    try :
        if len(room[i]) == width:
            map_room.append(room[i])
        else :
            print("Invalid map input.")
            err = True
            frist = True
            break
        if "F" in room[i]:
            q3.enQueue((room[i].index("F"),i))
            start = True
    except :
        print("Invalid map input.")
        err = True
        frist = True
        break
else :
    if len(map_room) != height :
        print("Invalid map input.")
        frist = True
        err = True
if not start :
    err = True
    if not frist:
        print("Invalid map input.")
if not err :
    # print('\n'.join(map_room))
    print(f"Queue: {q3.items}")
    while not q3.isEmpty() :
        x , y = q3.deQueue()
        q1.enQueue((x,y))
        for move_x , move_y in move_ment :
            if ( x+move_x >= 0 and x+move_x < width ) and ( y+move_y >= 0 and y+move_y < height) :
                if map_room[y+move_y][x+move_x] == "_" :
                    list_move = q1.items
                    list_will_move = q3.items
                    if ( x+move_x , y+move_y ) not in list_move and ( x+move_x , y+move_y ) not in list_will_move :
                        q3.enQueue(( x+move_x , y+move_y ))
                elif map_room[y+move_y][x+move_x] == "O" :
                    exit_room = False
                    err = True
                    print("Found the exit portal.")
                    q3.clear()
                    break
        if not q3.isEmpty():
            print(f"Queue: {q3.items}")
if not err :
    print("Cannot reach the exit portal.")