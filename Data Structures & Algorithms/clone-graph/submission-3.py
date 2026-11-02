"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        # Hash map to store the mapping from original node to its clone
        old_to_new = {}
        def dfs_clone(node):
            if node in old_to_new:
                return old_to_new[node]
            copy=Node(node.val)
            old_to_new[node]=copy
            for n in node.neighbors:
                copy.neighbors.append(dfs_clone(n))
            return copy
        return dfs_clone(node) 