import math
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.sqrt(n))
        bulbs = [True for i in range(n)]
        for T in range(2,n+1):
            for i in range(T-1,n,T):
                bulbs[i] = not bulbs[i]
        return(sum(bulbs))

print(Solution().bulbSwitch(9999999))