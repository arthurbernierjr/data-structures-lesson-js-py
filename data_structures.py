from collections import deque

# --- LinkedList ---
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self, data):
        self.head = Node(data, self.head)

    def size(self):
        counter = 0
        node = self.head
        while node:
            counter += 1
            node = node.next
        return counter

    def get_first(self):
        return self.head

    def get_last(self):
        if not self.head:
            return None
        node = self.head
        while node:
            if not node.next:
                return node
            node = node.next

    def clear(self):
        self.head = None

    def remove_first(self):
        if not self.head:
            return
        self.head = self.head.next

    def remove_last(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        previous = self.head
        node = self.head.next
        while node.next:
            previous = node
            node = node.next
        previous.next = None

    def insert_last(self, data):
        last = self.get_last()
        if last:
            last.next = Node(data)
        else:
            self.head = Node(data)

    def get_at(self, index):
        counter = 0
        node = self.head
        while node:
            if counter == index:
                return node
            counter += 1
            node = node.next
        return None

    def remove_at(self, index):
        if not self.head:
            return
        if index == 0:
            self.head = self.head.next
            return
        previous = self.get_at(index - 1)
        if not previous or not previous.next:
            return
        previous.next = previous.next.next

    def insert_at(self, data, index):
        if not self.head:
            self.head = Node(data)
            return
        if index == 0:
            self.head = Node(data, self.head)
            return
        previous = self.get_at(index - 1) or self.get_last()
        node = Node(data, previous.next)
        previous.next = node

# --- Stack ---
class Stack:
    def __init__(self):
        self.data = []

    def push(self, record):
        self.data.append(record)

    def pop(self):
        return self.data.pop()

    def peek(self):
        if not self.data:
            return None
        return self.data[-1]

# --- Queue ---
class Queue:
    def __init__(self):
        self.data = deque()

    def enqueue(self, record):
        self.data.appendleft(record)

    def dequeue(self):
        return self.data.pop()

# --- Binary Search Tree ---
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = BSTNode(value)
        if self.root is None:
            self.root = new_node
            return self

        current = self.root
        while True:
            if value == current.value:
                return None  # Or handle as an error/update
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return self
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return self
                current = current.right

    def find(self, value):
        if self.root is None:
            return None
        current = self.root
        while current:
            if value == current.value:
                return current
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return None

    def contains(self, value):
        return self.find(value) is not None

    def delete(self, value):
        self.root = self._delete_node(self.root, value)

    def _delete_node(self, node, value):
        if node is None:
            return None

        if value < node.value:
            node.left = self._delete_node(node.left, value)
        elif value > node.value:
            node.right = self._delete_node(node.right, value)
        else:
            if node.left is None and node.right is None:
                return None
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            temp = self._min_value_node(node.right)
            node.value = temp.value
            node.right = self._delete_node(node.right, temp.value)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def bfs(self):
        if not self.root:
            return []
        
        data = []
        queue = deque([self.root])

        while queue:
            node = queue.popleft()
            data.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return data

    def dfs_pre_order(self):
        data = []
        def traverse(node):
            if node:
                data.append(node.value)
                traverse(node.left)
                traverse(node.right)
        traverse(self.root)
        return data

    def dfs_post_order(self):
        data = []
        def traverse(node):
            if node:
                traverse(node.left)
                traverse(node.right)
                data.append(node.value)
        traverse(self.root)
        return data

    def dfs_in_order(self):
        data = []
        def traverse(node):
            if node:
                traverse(node.left)
                data.append(node.value)
                traverse(node.right)
        traverse(self.root)
        return data
