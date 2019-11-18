class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        result = 0
        while len(arr) > 1:
            min_index = arr.index(min(arr))
            
            if min_index > 0 and min_index < len(arr)-1:
                second_index = (min_index - 1) if arr[min_index - 1] <= arr[min_index + 1] else (min_index + 1)
            else:
                second_index = 1 if min_index == 0 else min_index - 1
            result += arr[second_index] * arr[min_index]
                # result +=  arr[1 if min_index == 0 else min_index - 1] * arr[min_index]
            arr.pop(min_index) 
        print(result)
arr = [6,2,4]
Solution().mctFromLeafValues(arr)
        