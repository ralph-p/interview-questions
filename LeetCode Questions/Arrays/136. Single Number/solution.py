class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = {}
        for n in nums:
            try:
                hash_table.pop(n)
            except:
                hash_table[n] = 1
        return hash_table.popitem()[0]

print(Solution().singleNumber([-2,1,-2]))