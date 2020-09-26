"""

note:
1. finding the shortest distance to zeros from zeros is easier than from ones
2. using multi-source BFS (from zeros) and a matrix records both answer and wheather the nodes have been visited (-1)

time complexity: O(R*C)
space complexity: O(1)

Runtime: 636 ms, faster than 87.12%
Memory Usage: 17.2 MB, less than 14.30%

"""

from collections import deque
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        
        # the problem ensures there at least a zero
        R = len(matrix)
        C = len(matrix[0])
        
        # create a matrix with same dimensions and -1 means unseen
        # [e]*n is faster then list comprehension create n items
        result = [[-1]*C for r in range(R)]
        
        queue = deque()
        
        # inversely start with zeros to find distance with ones 
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    queue.append((r,c))
                    result[r][c] = 0
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in [(0,-1),(-1,0),(0,1),(1,0)]:
                
                new_r = r + dr
                new_c = c + dc
                
                # if the neighbor cells are valid and haven't seen before
                # then the shortest distance of neighbor cells to zeros is the current one + 1
                if (0 <= new_r < R) and (0 <= new_c < C) and (result[new_r][new_c] == -1):
                    result[new_r][new_c] = result[r][c] + 1
                    queue.append((new_r, new_c))
         
        return result