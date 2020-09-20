"""

note:
1. two pointer can only be run on sorted arrays
2. the problem requires to return original index, so need to create a new array with both number and its original index

time complexity: O(nlogn)
space complexity: O(2n)->O(n)

Runtime: 64 ms, faster than 48.38%
Memory Usage: 15.4 MB, less than 18.22%

"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # two pointer techniques require the array to be sorted
        # since original index are required, so it has to keep that info by creating a new list with element in (num, ori_idx)
        sorted_nums = [(num, i) for i, num in enumerate(nums)]
        sorted_nums.sort()       
        
        l, r = 0, len(nums) - 1
        
        # cannot be the same element, so equal sign is not needed
        while r > l:
            
            two_sum = sorted_nums[l][0] + sorted_nums[r][0]
            
            if two_sum == target:
                # exactly one answer exists
                return [sorted_nums[l][1], sorted_nums[r][1]]
            
            elif two_sum > target:
                # two sum is larger than target, so we need to move r to smaller element
                # the possibility of smaller l is checked already, so no need to consider that
                r -= 1
            
            else:
                l += 1
            
            
        
        
"""
Alternative O(n) hash table solution

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # record seen numbers' position
        num_map = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # connections between any two elements can be checked from one direction, ex. all from latter element
            # so we can check existence in one pass but still ensure all possibilities are checked
            
            if complement in num_map:
                
                # only one answer is ensured
                return [num_map[complement], i]
        
            num_map[num] = i
"""