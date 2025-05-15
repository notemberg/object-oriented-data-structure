def linear_search_unordered(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i  
    return -1  

def sentinel_search(arr, key):
    n = len(arr)
    last = arr[-1]
    arr[-1] = key
    i = 0
    while arr[i] != key:
        i += 1
    arr[-1] = last  
    if i < n - 1 or arr[-1] == key:
        return i  
    return -1  

def move_to_front(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            arr.insert(0, arr.pop(i))  
            return i  
    return -1  

def transposition_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            if i != 0:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]  
            return i  
    return -1  

def linear_search_ordered(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i  
        elif arr[i] > key:
            break  
    return -1 

def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid  
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1  

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if node is None:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key)
        return node

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node 
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
result_node = bst.search(15)
if result_node:
    print("Key found:", result_node.key)
else:
    print("Key not found")


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            index = (index + 1) % self.size  
            if index == original_index:
                raise Exception("Hash table is full")
        self.table[index] = (key, value)

    def search(self, key):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]  
            index = (index + 1) % self.size
            if index == original_index:
                break  
        return None  

    def delete(self, key):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None  
                return True
            index = (index + 1) % self.size
            if index == original_index:
                break  
        return False  

ht = HashTable(10)
ht.insert(5, "Value1")
ht.insert(15, "Value2")
print(ht.search(5))  
print(ht.search(15))  
print(ht.search(10))  
ht.delete(5)
print(ht.search(5)) 

arr = [29, 15, 88, 42, 67, 5, 18]
key_to_find = 42


index = linear_search_unordered(arr, key_to_find)


if index != -1:
    print(f"Key {key_to_find} found at index {index}")
else:
    print(f"Key {key_to_find} not found")