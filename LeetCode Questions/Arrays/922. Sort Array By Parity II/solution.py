class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = []
        even = []
        returnArr = []
        for a in A:
            if a%2 == 0:
                even.append(a)
            else:
                odd.append(a)
        for i in range(len(A)):
            if i%2 == 0:
                returnArr.append(even.pop())
            else:
                returnArr.append(odd.pop())
        return returnArr

print(Solution().sortArrayByParityII([4,2,5,7]))