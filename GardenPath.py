class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        if N <= 4:
            return [i+1 for i in range(N)]
        path_map = [[] for i in range(N)]
        flowers = [0 for i in range(N)]
        for p in paths:
            path_map[p[0]-1].append(p[1])
            path_map[p[1]-1].append(p[0])
        for i in range(N):
            flowers[i] = ({1, 2, 3, 4} - {flowers[j] for j in path_map[i]}).pop()
        return flowers
            


N = 4
paths = [[1,2],[3,4]]
print(Solution().gardenNoAdj(N ,paths))