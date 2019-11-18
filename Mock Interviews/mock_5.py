class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        maj = len(nums)/2
        for n in num_set:
            if nums.count(n) >= maj:
                return n
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def helper(nums,target,left):
            low = 0
            high = len(nums)    
            # while low is less than high    
            while low < high:
                #find the mid point
                mid = (low + high) // 2
                # if the middle is greater than the target, move the high pointer to the mid point
                if nums[mid] > target or (left and target == nums[mid]):
                    high = mid
                else:
                    low = mid+1

            return low
        #find left index
        left_index = helper(nums, target, True)
        #find right index
        right_index = helper(nums,target,False)-1
        if left_index == len(nums) or nums[left_index] != target:
            return [-1,-1]
        return [left_index, right_index]

        
        
# print(Solution().majorityElement([3,2,3]))
print(Solution().searchRange(nums = [5,7,7,8,8,10], target = 8))