"""

note:
1. reversing can be thought as mirroring, so exchange every pair of elements at opposite side w.r.t the center

time complexity: O(n/2)->O(n)
space complexity: O(1)

Runtime: 204 ms, faster than 92.63%
Memory Usage: 18.2 MB, less than 78.06%

"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        l = 0
        r = len(s) - 1
        
        # if there is odd number of element then the loop stops at r = l
        while r > l:
            # OR s[l], s[r] = s[r], s[l]
            tmp = s[l]
            s[l] = s[r]
            s[r] = tmp
            
            r -= 1
            l += 1