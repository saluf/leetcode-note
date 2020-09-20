"""

note:
1. the problem required the result (squred) in non-decreasing order, but start from the largest one is easier

time complexity: O(n)
space complexity: O(1)

Runtime: 244 ms, faster than 59.95%
Memory Usage: 15.8 MB, less than 51.28%

"""

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        
        n = len(A)
        # create empty list with size = n
        result = [-1] * n
        
        # two pointers from each side
        # may be neg/pos, neg--/neg, or pos/pos++
        l = 0
        r = n - 1
        
        # loop through each element reversely
        for i in range(n-1, -1, -1):
            
            # fill the element with large one
            if abs(A[r]) >= abs(A[l]):
                result[i] = A[r]**2
                r -= 1
            else:
                result[i] = A[l]**2
                l += 1
            
        return result
        
"""
alternative solution with O(nlogn) complexity

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        
        result = []
        
        for num in A:
            result.append(num**2)
            
        return sorted(result)
"""