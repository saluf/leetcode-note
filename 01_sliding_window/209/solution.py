"""

note:
1. Keep track window condition by record sum of it
2. If condistion is satisfied, then shrink from left, and try to find shorter subarray. 
Because all shorter subarray not end at current "r" location is checked and not meet condition.
3. Use a very large number to cover edge case that sum of array is smaller than the target.

time complexity: O(2n) -> O(n)
space complexity: O(1)

Runtime: 80 ms, faster than 62.34%
Memory Usage: 16.2 MB, less than 76.69%

"""

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
                
        l = 0
        subsum = 0
        # init with a very large number (inf or len(nums) + 1) to 
        # cover the case if there is no subarray meet the condition
        shortest = float("inf")
        
        for r, num in enumerate(nums):
            
            subsum += num        
            # if condition is statisfied, it would try to shrink in size from left
            # why not shrink from right or could be in the middle? they are all checked during step by step extending
            while subsum >= s:
                shortest = min(shortest, r - l + 1)
                
                subsum -= nums[l]
                l += 1                
         
        # short hand to check if the variable shortest is changed or not
        return 0 if shortest == float("inf") else shortest