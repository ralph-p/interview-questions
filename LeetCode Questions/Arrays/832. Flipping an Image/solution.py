class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for a in A:
            a.reverse()
            for i,c in enumerate(a):
                a[i] = 1 if c == 0 else 0
        return(A)

arr = [[1,1,0],[1,0,1],[0,0,0]]
print(Solution().flipAndInvertImage(arr))

# [[1,0,0],[0,1,0],[1,1,1]]