class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None
class LRUCache:

    def __init__(self, capacity: int):
        self.left=Node(0,0)
        self.right=Node(0,0)
        self.c=capacity
        self.cache={}
        
        self.left.next=self.right
        self.right.prev=self.left
    def remove(self,node):
        prev,next=node.prev,node.next
        prev.next=next
        next.prev=prev
    def insert(self,node:Node):
        
        prev,next=self.right.prev,self.right
        prev.next=node
        next.prev=node
        node.next,node.prev=self.right,prev


    def get(self, key: int) -> int:
        if key in self.cache:
            node=self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node=Node(key,value)
        self.cache[key]=node
        self.insert(node)
        if len(self.cache)>self.c:
            leftnode=self.left.next
            self.remove(leftnode)
            del self.cache[leftnode.key]
        

        
