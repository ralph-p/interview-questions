class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        index = 0
        while index < len(arr):
            if arr[index] == 0:
                arr.insert(index,0)
                arr.pop()
                index += 2
            else:
                index += 1
arr = [1,0,2,3,0,4,5,0]
Solution().duplicateZeros(arr)
print(arr)