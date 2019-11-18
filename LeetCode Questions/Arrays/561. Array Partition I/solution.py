class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        total = 0
        while nums:
            total += min(nums.pop(),nums.pop())
        return total

print(Solution().arrayPairSum([1,4,3,2]))