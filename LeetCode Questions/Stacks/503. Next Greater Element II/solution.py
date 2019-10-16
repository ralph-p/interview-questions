class Solution(object):
    def nextGreaterElements(self, nums):
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

        
nums = [1,2,1]
print(Solution().nextGreaterElements(nums))