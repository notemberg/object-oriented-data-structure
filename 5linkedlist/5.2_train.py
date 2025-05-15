class Node:
    def __init__(self, elem=None):
        self.elem = elem
        self.prev = None
        self.next = None

class CircularDoublyLinkList:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def append(self, elem):
        node = Node(elem)
        if self.head is None:
            self.head = self.tail = node
            node.prev = node.next = node
        else:
            node.prev = self.tail
            node.next = self.head
            self.tail.next = node
            self.head.prev = node
            self.tail = node
        self.size += 1

def find_route_info(cl, source, destination):
    curr = cl.head
    while curr.elem != source:
        curr = curr.next

    f_route = ""
    f_number = 0
    b_route = ""
    b_number = 0

    node_f = curr
    while node_f.elem != destination:
        node_f = node_f.next
        f_route += f"->{node_f.elem}"
        f_number += 1

    node_b = curr
    while node_b.elem != destination:
        node_b = node_b.prev
        b_route += f"->{node_b.elem}"
        b_number += 1

    return f_route, f_number, b_route, b_number

print("***Railway on route***")
stations, sdd = input("Input Station name/Source, Destination, Direction(optional): ").split("/")
direction = sdd.split(",")[2] if len(sdd.split(",")) == 3 else ""

cl = CircularDoublyLinkList()

for s in stations.split(","):
    cl.append(s)

source, destination = sdd.split(",")[:2]
f_route, f_number, b_route, b_number = find_route_info(cl, source, destination)

if direction == "F" or (direction == "" and f_number < b_number):
    print(f"Forward Route: {source}{f_route},{f_number}")
elif direction == "B" or (direction == "" and b_number < f_number):
    print(f"Backward Route: {source}{b_route},{b_number}")
else:
    print(f"Forward Route: {source}{f_route},{f_number}")
    print(f"Backward Route: {source}{b_route},{b_number}")