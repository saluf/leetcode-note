"""

note:
1. fix a element and the problem reduced to 2 sum
2. compare and record smallest gap, because there is no guarantees that when the closest number will show up

time complexity: O(n^2)
space complexity: O(1)

Runtime: 124 ms, faster than 78.79% 
Memory Usage: 13.8 MB, less than 72.13%

"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        # record closest 
        closest_gap = float('inf')
        
        # 2sum requires the array to be sorted
        nums.sort()
        
        # fix a element and reduce problem to 2sum
        for fix in range(len(nums)-2):
            num = nums[fix]
            
            l = fix + 1
            r = len(nums) - 1
            
            while r > l:
                three_sum = num + nums[l] + nums[r] 
                
                # if find smaller gap, record it
                if abs(three_sum - target) < abs(closest_gap):
                    closest_gap = three_sum - target
                
                # no any gap smaller than 0, so return
                if three_sum == target:
                    return three_sum
                elif three_sum > target:
                    r -= 1
                else:
                    l += 1
                    
        return target + closest_gap