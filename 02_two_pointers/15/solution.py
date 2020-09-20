"""

note:
1. to find a + b + c, we can fix a and find b + c = -a (two sum)
2. to ensure no duplicated set of nums, i) skip duplicated a, ii) skip all b and c if a (a, b, c) set found 

time complexity: O(n^2)
space complexity: O(1)

Runtime: 924 ms, faster than 66.20%
Memory Usage: 17.1 MB, less than 79.39%

"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        
        if not nums or len(nums) <= 2:
            return result
        
        # two pointer technique requires array to be sorted
        nums.sort()
        if nums[0] > 0 or nums[-1] < 0:
            # all numbers are positive or negative
            return result
        
        for fix in range(len(nums)-2):
            num = nums[fix]
            if fix != 0 and num == nums[fix-1]:
                # skip the duplicated number
                continue
            
            l = fix + 1
            r = len(nums) - 1
            
            while r > l:
                two_sum = nums[l] + nums[r]
                # a + b + c = 0 --> if a is fixed, then b + c = -a
                if two_sum == -num:
                    result.append([num, nums[l], nums[r]]) 
                    
                    # skip duplicated numbers
                    while r > l and nums[r] == nums[r-1]:
                        r -= 1
                    while r > l and nums[l] == nums[l+1]:
                        l += 1
                    
                    # move both l & r, since a + b or a + c ensures the remain number
                    l += 1
                    r -= 1
                    
                elif two_sum > -num:
                    r -= 1
                else:
                    l += 1
                    
        return result