class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        length = len(nums)
        while i <= length:
            if nums[i] == 0:
                zero = nums.pop(i)
                nums.append(zero)
                length -= 1
            else:
                i+= 1
        return nums 

print(Solution().moveZeroes([0,0,1]))