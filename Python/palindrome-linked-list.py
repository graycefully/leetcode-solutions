# Time: O(N)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Find the middle of the linked list using the Hare-Tortoise 
        # algorithm.
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse the second half of the linked list.
        prev = None
        while slow:
            slow.next, slow, prev = prev, slow.next, slow

        # Compare the first half and the reversed second half.
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
        
