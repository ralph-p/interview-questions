class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        arr_d = []
        for i in range(left,right):
            nums = [int(d) for d in str(i)]
            for n in nums:
                alls = True
                if n and i % n != 0:
                    alls = False
            if alls:
                arr_d.append(n)
        print(arr_d)

Solution().selfDividingNumbers(1,22)