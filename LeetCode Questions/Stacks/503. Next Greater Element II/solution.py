class Solution(object):
    def nextGreaterElements_1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        c_a = []
        for i in range(0,len(nums)-1):
            gt = -1
            if nums[i] == max(nums):
                c_a.append(gt)
            else:
                if i == len(nums)-1:
                    current_index = 0
                else:
                    current_index = i + 1
                while current_index != i:
                    print(nums)
                    if current_index > len(nums)-1:
                        current_index = 0
                    if nums[current_index] > nums[i]:
                        gt = nums[current_index]
                        break
                    current_index += 1
            c_a.append(gt)
        return c_a
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        next_greater = []
        for i,n in enumerate(nums):
            gt = []
            passed = False
            for x in range(len(nums)):
                if x == i:
                    passed = True
                    continue
                if nums[x] > n:
                    if passed:
                        gt = [nums[x]]
                        break
                    else:
                        gt.append(nums[x])
            if len(gt) == 0:
                next_greater.append(-1)
            else:
                next_greater.append(gt[0])
        return next_greater
        
        
nums = [5,4,3,2,1]
# [-1,5,5,5,5]
print(Solution().nextGreaterElements(nums))
