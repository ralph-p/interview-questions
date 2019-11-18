class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        stack = []
        for i in range(len(nums)):
            stack.append([i,target-nums[i]])
        while stack:
            x = stack.pop(0)
            for i in range(x[0],len(nums)):
                if i != x[0]:
                    if nums[i] == x[1]:
                        return [x[0],i]
    def prisonAfterNDays(self, cells, N):
            def nextday(cells):
                return [int(i > 0 and i < 7 and cells[i-1] == cells[i+1]) for i in range(8)]
            seen = {}
            while N > 0:
                c = tuple(cells)
                if c in seen:
                    N %= seen[c] - N
                seen[c] = N

                if N >= 1:
                    N -= 1
                    cells = nextday(cells)

            return cells


# print(Solution().twoSum(nums = [3,2,4], target = 6))
print(Solution().prisonAfterNDays(cells = [0,1,0,1,1,0,0,1], N = 7))