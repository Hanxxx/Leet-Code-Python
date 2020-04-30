"""
two-pass solution
"""
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if n == 0:
            return head
        cnt = 0
        cur = head
        while cur != None:
            cnt += 1
            cur = cur.next
        root = ListNode(-1)
        root.next = head
        cur = root
        for i in range(cnt - n):
            cur = cur.next
        if cur.next != None:
            cur.next = cur.next.next
        
        return root.next