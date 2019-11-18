class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        index = 0
        while index < n:
            if nums[index] == val:
                nums.pop(index)
                n = len(nums)
            else:
                index += 1
        return len(nums)
    def combinationSum(self, candidates, target):
        answers = []
        candidates.sort()
        def helper(c,target,arr):
            if target == 0:
                answers.append(arr)
            for i,n in enumerate(c):
                if target >= n:
                    helper(c[i:],target-n,arr + [n])
                else:
                    break
        helper(candidates,target,[])
        return(answers)

nums = [0,1,2,2,3,0,4,2]
val = 2
Solution().removeElement(nums,val)
Solution().combinationSum(candidates = [2,3,6,7], target = 7)