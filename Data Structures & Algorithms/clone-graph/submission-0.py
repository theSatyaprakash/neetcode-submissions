"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        # Hash map to store the mapping from original node to its clone
        old_to_new = {}
        
        # Clone the starting node and put it in the map
        old_to_new[node] = Node(node.val)
        
        # Queue for BFS traversal
        queue = deque([node])
        
        while queue:
            current = queue.popleft()
            
            # Iterate through all the neighbors of the current node
            for neighbor in current.neighbors:
                if neighbor not in old_to_new:
                    # Clone the neighbor and store it in the hash map
                    old_to_new[neighbor] = Node(neighbor.val)
                    # Add the original neighbor to the queue to visit later
                    queue.append(neighbor)
                
                # Add the cloned neighbor to the current cloned node's neighbor list
                old_to_new[current].neighbors.append(old_to_new[neighbor])
                
        return old_to_new[node]