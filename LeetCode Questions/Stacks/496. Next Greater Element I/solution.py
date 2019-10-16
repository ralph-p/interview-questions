class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        new_numbers = []
        for i in nums1:
            stack = self.fill_stack(nums2)
            gt = -1
            while stack:
                next_num = stack.pop(0)
                print(next_num)
                if next_num == i:
                    while next_num <= i and stack:
                        next_num = stack.pop(0)
                    if next_num > i:
                        gt = next_num
            new_numbers.append(gt)
        return new_numbers
    def fill_stack(self,nums2):
        stack = []
        for n in nums2:
            stack.append(n)
        return stack
nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(Solution().nextGreaterElement(nums1,nums2))