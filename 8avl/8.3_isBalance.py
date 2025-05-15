class TreeNode(object): 
    def __init__(self, val): 
        self.data = val 
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.data)
  
class AVL_Tree(object): 
    def __init__(self):
        self.root = None



    def getHeight(self,node):
        if not node:
            return 0
        return node.height
    
    def getBalance(self,node):
        if not node:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def rightRotate(self,y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1+max(self.getHeight(y.left),self.getHeight(y.right))
        x.height = 1+max(self.getHeight(x.left),self.getHeight(x.right))

        return x
    def leftRotate(self,x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1+max(self.getHeight(x.left),self.getHeight(x.right))
        y.height = 1+max(self.getHeight(y.left),self.getHeight(y.right))

        return y

    def insert(self,node,data):
        if not node:
            return TreeNode(data)

        if data < node.data:
            node.left = self.insert(node.left,data)
        elif data > node.data:
            node.right = self.insert(node.right,data)

        node.height = 1 + max(self.getHeight(node.left),self.getHeight(node.right))
        balance = self.getBalance(node)

        if balance > 1 and self.getBalance(node.left) >= 0:
            print("Right Right Rotation")
            
            return self.rightRotate(node)

        # Left Right
        if balance > 1 and self.getBalance(node.left) < 0:
            print("Right Left Rotation")
            
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)

        # Right Right
        if balance < -1 and self.getBalance(node.right) <= 0:
            print("Left Left Rotation")
            return self.leftRotate(node)

        # Right Left
        if balance < -1 and self.getBalance(node.right) > 0:
            print("Left Right Rotation")
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        return node

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)
  
myTree = AVL_Tree() 
root = None

print(" *** AVL Tree Insert Element ***")
data = input("Enter Input : ").split()
for e in data:
    print("insert :",e)
    root = myTree.insert(root, int(e))
    printTree90(root)
    print("====================")
