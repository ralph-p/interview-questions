class Solution(object):
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        if len(A) == K or K == 1:
            return sum(A)
        dp = [[0 for i in range(len(A))] for i in range(len(A))]
        for j in range(0,len(A)):
            for i in range(j,len(A)):
                if j == i:
                    dp[j][i] = A[j]
                else:
                    dp[j][i] = A[i] + dp[j][i-1]
        max_arr = [0] * len(A)
        for i in range(1,len(A)+1):
            max_arr[i-1] = dp[i-1][i-1]
            end = min(len(A) - K+1,len(A)-i)
            for j in range(0,end):
                if (dp[i-1][j+i-1]/(j+1)) > max_arr[i-1]:
                    max_arr[i-1] = (dp[i-1][j+i-1]/(j+1))
        max_arr.sort(reverse=True)
        print(max_arr)
        return(sum(max_arr[:K]))

A = [9,1,2,3,9]
K = 3
print(Solution().largestSumOfAverages(A,K))