"""

note:
1. position l and r form a window
2. hashmap record the last position of the char instead of occurence
3. if char is repeated in the window (i.e. l <= char_map[char]), move l to char_map[char], so reptition is removed
4. since every time encounter repetition, l moves, so it can be ensured that no more repetiton after that move

time complexity: O(n)
space complexity: O(1)

Runtime: 52 ms, faster than 92.13%
Memory Usage: 14.1 MB, less than 20.32%
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        char_map = {}
        max_length = 0
        
        l = 0
        
        for r, char in enumerate(s):
            
            if char in char_map and char_map[char] >= l:
                # the duplicated char is in the window
                # shif l to next position to ensure the char is not duplicated
                l = char_map[char] + 1
            
            # record last position
            char_map[char] = r
            
            # if statement is faster than max()
            if r - l + 1 > max_length:
                max_length = r - l + 1
        
        return max_length