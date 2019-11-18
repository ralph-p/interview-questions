class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        while i <= len(nums)-1:
            if nums[i] == target:
                return i
            elif nums[i] < target:
                i += 1
            elif nums[i] > target:
                return i 
        return i


print(Solution().searchInsert([1,3,5,6], 2))