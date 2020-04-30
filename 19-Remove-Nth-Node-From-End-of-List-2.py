"""
one-pass solution
"""
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head == None:
            return
        root = ListNode(-1)
        root.next = head
        cur = root
        n_ahead = cur
        for i in range(n + 1):
            n_ahead = n_ahead.next
        while n_ahead != None:
            cur = cur.next
            n_ahead = n_ahead.next
        cur.next = cur.next.next
        return root.next
            