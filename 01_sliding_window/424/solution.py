"""

note:
1. k opeartions to change letters equals allowing k minority characters in the window
2. the most frequent letter can be unchanged or changed to new letter (ex. Before extending the window 
"A" is most frequent letter, and then "B" was added. After that "B" is more than "A", so it changes.)
3. window validation condition : (window size) - most_frequent_letter_count <= k
(if true -> extending, otherwise -> sliding)

time complexity: O(n)
space complexity: O(26) -> O(1)

Runtime: 80 ms, faster than 98.90%
Memory Usage: 13.7 MB, less than 93.20%

"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # catch empty string case
        if not s : return 0
        
        letter_count = {}
        l = 0
        most_f = 0
        
        for r, letter in enumerate(s):
            
            # update letter count map
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
                
            # get most frequent letter. It can be either the origin most frequent letter or the current letter
            most_f = max(most_f, letter_count[letter])
            
            # check if current window matches condition then slide the window
            if (r - l + 1) - most_f > k:
                letter_count[s[l]] -= 1
                l += 1
                
        return r - l + 1