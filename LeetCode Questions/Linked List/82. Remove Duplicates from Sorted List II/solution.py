# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        def find_next(head):
            if head.next == None:
                return None
            elif head.next.val == head.val:
                find_next(head.next)
            else:
                return head.next
        while head.next:
            if head.val == head.next.val:
                head.next = find_next(head)
            else:
                head = head.next
        return head

