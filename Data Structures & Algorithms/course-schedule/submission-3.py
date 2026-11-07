from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Build the adjacency list and in-degree array
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        
        for dest, src in prerequisites:
            adj[src].append(dest)
            in_degree[dest] += 1
            
        # Step 2: Push all nodes with an in-degree of 0 into the queue
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        # Step 3: Process the queue and remove edges
        completed_courses = 0
        
        while queue:
            node = queue.popleft()
            completed_courses += 1
            
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        # Step 4: If we processed all courses, there are no cycles
        
        return completed_courses == numCourses