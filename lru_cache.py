"""
LRU CACHE
"""


class Node:
    def __init__(self,key,value):
        self.key = key
        self.value=value
        self.prev=None
        self.next=None


class LRUCache:
    def __init__(self,capacity):
        self.capacity=capacity
        self.cache = {}

        self.head=Node(0,0)
        self.tail=Node(0,0)

        self.head.next=self.head
        self.tail.next=self.tail


    def remove(self,node):
        prev_node = node.prev
        next_node=node.next

        prev_node.next=next_node
        next_node.prev=prev_node



    def __repr__(self):
        return f"{self.head},{self.tail},{self.head.next},{self.tail.next}"



node=LRUCache(3)
print(node)