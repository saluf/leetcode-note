"""

note:
1. Dummy head can help hold the linked list, if there is a chance that head will be changed.
2. Use fast-slow two pointers. The slow one is responsible to create new links, the fast one is responsible to explore the duplicated
3. If duplicated nodes found, then (slow.next != fast) holds. Use this condition to remove nodes. Otherwise move one step each.

time complexity: O(n)
space complexity: O(1)

Runtime: 40 ms, faster than 80.45%
Memory Usage: 13.9 MB, less than 27.05%

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        # head may change, so use dummy head to hook it
        dummy_head = ListNode(-1)
        dummy_head.next = head
        
        # slow and fast two pointers
        # slow one is responsible to create new links, fast one is responsible to explore the duplicated
        slow = dummy_head
        fast = head
        
        while fast is not None:
            
            # move fast pointer to last duplicted number
            while (fast.next is not None) and (fast.next.val == fast.val):
                fast = fast.next
                

            if (slow.next != fast):
                # remove all repeated nodes by skipping them
                slow.next = fast.next
                fast = fast.next
            
            else:
                # no repeated nodes, move ordinarily
                slow = slow.next
                fast = fast.next
            
        return dummy_head.next