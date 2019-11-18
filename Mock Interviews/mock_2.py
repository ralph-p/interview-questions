# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = 
import random
class Solution(object):
    def pivotIndex(self, nums):
        total_sum = sum(nums)
        left = 0
        for i,j in enumerate(nums):
            total_sum -= j
            if total_sum == left:
                return i
            left += j
        return -1
class Solution_1(object):
    
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
    def getSize(self):
        temp = self.head
        size = 0
        while temp.next:
            size += 1
            temp = temp.next
        return size
    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        temp = self.head
        for i in range(0,random.randint(0,self.getSize())):
            temp = temp.next
        return temp.val

nums = [-1,-1,-1,-1,-1,-1]
print(Solution().pivotIndex(nums))