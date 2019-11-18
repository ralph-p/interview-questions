class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        def empty_map(hash_map):
            for m in hash_map:
                if m[0] > 0:
                    return False
            return True
        if not n:
            return tasks
        hash_map = [[0,0] for i in range(26)]
        p_queue = []
        for t in tasks:
            hash_map[ord(t)-65][0]+= 1
        while not empty_map(hash_map):
            print(p_queue)
            for i,e in enumerate(hash_map):
                if e[0] > 0:
                    if e[1] == 0 or (len(p_queue)-e[1]) > n:
                        p_queue.append(chr(i+65))
                        hash_map[i][0] -= 1
                        hash_map[i][1] = i+1
                    elif (i-e[1]) <= n:
                        p_queue.append("IDLE")
                        continue


        return p_queue

tasks = ["A","A","A","B","B","B"]
n = 2
print(Solution().leastInterval(tasks, n))