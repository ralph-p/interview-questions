# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        L, R, answer = [0]*length, [0]*length, [0]*length
        L[0] = 1
        R[length - 1] = 1
        for i in range(1,length):
            L[i] = nums[i-1] * L[i-1]
        for i in reversed(range(length - 1)):
            R[i] = nums[i + 1] * R[i + 1]
        for i in range(length):
            answer[i] = L[i] * R[i]
        return answer
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum_1 = 0
        sum_2 = 0
        carry = 0
       
        temp = l1.val + l2.val
        if temp >= 10:
            carry = 1
            temp -= 10
        ans = [temp]
        while l1.next or l2.next:
            if l1.next:
                l1 = l1.next
            else:
                l1 = ListNode(0)
            if l2.next:
                l2 = l2.next
            else:
                l2 = ListNode(0)
            temp = l1.val + l2.val + carry
            if temp >= 10:
                carry = 1
                temp -= 10
            else:
                carry = 0
            ans.append(temp)
        dummy = node_ans = ListNode(ans[0])
        for a in range(1,len(ans)):
            node_ans.next = ListNode(ans[a])
            node_ans = node_ans.next
        if carry:
            node_ans.next = ListNode(carry)
            node_ans = node_ans.next
            
        return dummy
    def isValidBST(self, root):
        INT_MAX = 4294967296
        INT_MIN = -4294967296
        def check_bst(root,mini,maxi):
            if not root:
                return True
            if root.val < mini or root.val > maxi:
                return False
            return (check_bst(root.left,mini,root.val-1) 
                    and check_bst(root.right,root.val+1,maxi))
            
        return check_bst(root,INT_MIN,INT_MAX)
print(Solution().productExceptSelf([1,2,3,4]))