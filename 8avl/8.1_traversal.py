class AVLTree:
    class AVLNode:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right
            self.height = self.setHeight()

        def __str__(self):
            return str(self.data)

        def setHeight(self):
            a = self.getHeight(self.left)
            b = self.getHeight(self.right)
            self.height = 1 + max(a, b)
            return self.height

        def getHeight(self, node):
            return -1 if node is None else node.height

        def balanceValue(self):
            return self.getHeight(self.left) - self.getHeight(self.right)

    def __init__(self, root=None):
        self.root = root

    def add(self, data):
        if self.root is None:
            self.root = self.AVLNode(data)
        else:
            self.root = self._add(self.root, data)  

    def _add(self, node, data):
        if node is None:
            return self.AVLNode(data)

        if data < node.data:
            node.left = self._add(node.left, data)
        elif data >= node.data:
            node.right = self._add(node.right, data)

        node.setHeight()
        balance = node.balanceValue()

        # Left Left
        if balance > 1 and node.left.balanceValue() >= 0:
            return self.rotateRightChild(node)

        # Left Right
        if balance > 1 and node.left.balanceValue() < 0:
            node.left = self.rotateLeftChild(node.left)
            return self.rotateRightChild(node)

        # Right Right
        if balance < -1 and node.right.balanceValue() <= 0:
            return self.rotateLeftChild(node)

        # Right Left
        if balance < -1 and node.right.balanceValue() > 0:
            node.right = self.rotateRightChild(node.right)
            return self.rotateLeftChild(node)

        return node

    def rotateLeftChild(self, x):
        y = x.right
        T = y.left
        y.left = x
        x.right = T
        x.setHeight()
        y.setHeight()
        return y

    def rotateRightChild(self, y):
        x = y.left
        T = x.right
        x.right = y
        y.left = T
        y.setHeight()
        x.setHeight()
        return x

    def postOrder(self):
        print("AVLTree post-order : ", end="")
        self._postOrder(self.root)
        print()

    def _postOrder(self, root):
        if root is None:
            return
        self._postOrder(root.left)
        self._postOrder(root.right)
        print(root.data, end=" ")

    def printTree(self):
        self._printTree(self.root)
        print()

    def _printTree(self, node, level=0):
        if node is not None:
            self._printTree(node.right, level + 1)
            print('     ' * level, node.data)
            self._printTree(node.left, level + 1)

avl1 = AVLTree()
inp = input('Enter Input : ').split(',')

for i in inp:
    if i[:2] == "AD":
        avl1.add(int(i[3:]))
    elif i[:2] == "PR":
        avl1.printTree()
    elif i[:2] == "PO":
        avl1.postOrder()
