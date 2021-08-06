class Node:

    def __init__(self, key: str, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:

    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None for _ in range(self.capacity)]

    def hash_func(self, key: str) -> int:
        return sum([ord(ch) for ch in key]) % self.capacity

    def search(self, key: str):
        idx = self.hash_func(key)
        node = self.table[idx]
        while node and node.key != key:
            node = node.next
        if node:
            return node.value
        else:
            return None

    def insert(self, key: str, value):
        idx = self.hash_func(key)
        node = self.table[idx]
        if not node:
            self.table[idx] = Node(key, value)
        else:
            while node.next:
                node = node.next
            node.next = Node(key, value)

    def delete(self, key: str):
        idx = self.hash_func(key)
        node = self.table[idx]
        prev = None
        while node and node.key != key:
            prev = node
            node = node.next
        if not node:
            return None
        else:
            result = node.value
            if prev:
                prev.next = node.next
            else:
                self.table[idx] = node.next
            return result
