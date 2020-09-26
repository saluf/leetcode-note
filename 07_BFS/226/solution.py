"""

note:
1. invert a binary tree by swapping left and right subtree level by level

time complexity: O(n)
space complexity: O(n/2 + 1) -> O(n)

Runtime: 24 ms, faster than 94.05%
Memory Usage: 13.9 MB, less than 25.90%

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        if root is None:
            return root
        
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            
            # swap left and right subtree
            tmp = node.left
            node.left = node.right
            node.right = tmp
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        return root