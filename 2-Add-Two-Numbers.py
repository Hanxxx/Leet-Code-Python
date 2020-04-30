class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        ret_root = ListNode(-1)
        cur = ret_root
        while l1 != None and l2 != None:
            carry, result = divmod(l1.val + l2.val + carry, 10)
            l1 = l1.next
            l2 = l2.next
            cur.next = ListNode(result)
            cur = cur.next

        rest = l1 if l2 == None else l2
        while rest != None:
            carry, result = divmod(rest.val + carry, 10)
            cur.next = ListNode(result)
            cur = cur.next
            rest = rest.next
            
        if carry != 0:
            cur.next = ListNode(carry)
            
        return ret_root.next