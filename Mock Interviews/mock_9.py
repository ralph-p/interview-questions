from math import log10
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        while (n != 1):
            if (n % 2 != 0):
                return False
            n = n//2
        return True
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # For each number i in nums,
        # mark the number that i points as negative.
        # positive numbers mark the index that has missing values
        # look through the list for positive values and append that to the missing element array
        if not nums:
            return nums
        n = len(nums)
        missing = []
        for i in range(n):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])
        for i,n in enumerate(nums):
            if n > 0:
                missing.append(i+1)
        return missing

print(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print(Solution().findDisappearedNumbers([1,1]))
# print(Solution().isPowerOfTwo(-16))