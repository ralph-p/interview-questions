class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if not n:
            return tasks
        task_q = []
        index = 0
        while tasks:
            print(tasks)
            if not task_q:
                task_q.append(tasks.pop(0))
            else:
                if tasks[index] == task_q[-1]:
                    index += 1
                else:
                    if tasks[index] == task_q[index-n]:
                        task_q.append("I")
                        index += 1
                    else:
                        task_q.append(tasks.pop(index)) 
            if index >= len(tasks):
                index = 0
        return task_q
        return len(task_q)
        return "".join(task_q)


print(Solution().leastInterval(tasks = ["Program","Program","Program","Read","Play Guitar","Read"], n = 2))