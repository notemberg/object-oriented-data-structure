class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(node.right, data)

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    # Method to swap left and right nodes
    def swap(self, node):
        if node is None:
            return
        
        node.left, node.right = node.right, node.left
        
        self.swap(node.left)
        self.swap(node.right)

    # Inorder Traversal (left, root, right)
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=' ')
            self.inorder(node.right)

    # Preorder Traversal (root, left, right)
    def preorder(self, node):
        if node:
            print(node.data, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    # Postorder Traversal (left, right, root)
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=' ')

# Example usage 4 5 6 1 2 3 8 7 9
T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    T.insert(i)

print("Original Tree:")
T.printTree(T.root)

# Traversals
print("\nInorder Traversal:")
T.inorder(T.root)
print("\nPreorder Traversal:")
T.preorder(T.root)
print("\nPostorder Traversal:")
T.postorder(T.root)

# Call the swap method
T.swap(T.root)
print("\nTree after swapping left and right nodes:")
T.printTree(T.root)
