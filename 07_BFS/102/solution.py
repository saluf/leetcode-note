"""

note:
1. use queue to implementt BFS to realize level-order traversal
2. push node and level information into queue for while loop to identify the level of the node, and create or append to the corresponding list

time complexity: O(n)
space complexity: O(n/2 + 1) -> O(n)

Runtime: 32 ms, faster than 84.46%
Memory Usage: 14.3 MB, less than 19.67%

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if root is None:
            return []
            
        result = []
        # create and init a queue with level information
        queue = deque([[root, 0]])
        
        while queue:
            node, lvl = queue.popleft()
            
            # list[lvl] requires a list of values of the elements in that lvl
            # if length of result array does not equal to lvl + 1 -> it is the 1st element in that lvl
            # create a list, otherwise append a new element
            if len(result) == lvl + 1:
                result[lvl].append(node.val)
            else:
                result.append([node.val])
                
            if node.left:
                queue.append([node.left, lvl+1])
            if node.right:
                queue.append([node.right, lvl+1])
            
        return result