class Node:
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None
        
class LRUCache:
    def __init__(self, capacity: int):
        self.hash = {} # key -> value
        self.capacity = capacity
        self.head = self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.hash:
            return -1
        else:
            n = self.hash[key]
            # move node to front of list  
            self.removeNode(n)
            self.insertToFront(n)
            return n.value

    def put(self, key: int, value: int) -> None:     
        if key in self.hash:
            self.hash[key].value = value
            n = self.hash[key]
            self.removeNode(n)
            self.insertToFront(n)
            
        else:
            n = Node()
            n.key = key
            n.value = value
            # insert node to the front of list
            self.insertToFront(n)
            self.hash[key] = n
            self.size += 1
            if self.size > self.capacity:
                n = self.tail.prev
                del self.hash[n.key]
                self.removeNode(n)
                self.capacity -= 1
    
    def insertToFront(self, n):
        current_head = self.head.next
        self.head.next = n
        n.next = current_head
        current_head.prev = n
        n.prev = self.head
    
    def removeNode(self, n):
        n.next.prev = n.prev
        n.prev.next = n.next