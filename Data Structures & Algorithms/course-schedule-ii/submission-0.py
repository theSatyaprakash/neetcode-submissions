from collections import defaultdict, deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build adjacency list and in-degree array
        adj = defaultdict(list)
        in_degree = [0] * numCourses
        
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            in_degree[course] += 1
            
        # Queue for courses with no prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        res = []
        
        while queue:
            curr = queue.popleft()
            res.append(curr)
            
            # Decrement in-degree of neighboring courses
            for neighbor in adj[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        # Return result if all courses can be finished, else empty list
        return res if len(res) == numCourses else []