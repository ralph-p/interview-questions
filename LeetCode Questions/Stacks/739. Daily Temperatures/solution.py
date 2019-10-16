class Solution(object):
    def dailyTemperatures(self, T):
        answer = [0] * len(T)
        # create empty stack
        stack = []
        for i in range(0,len(T)):
            # create a temp from the current index
            t = T[i]
            # while there is something in the stack and
            # the last element in the stack is colder than the current temp
            while stack and T[stack[-1]] < t:
                # pop from the stack and get the index value
                current = stack.pop()
                # set value of the answer at index current to index - current index
                answer[current] = i - current
            # add the latest index to the stack
            stack.append(i)
            print(stack)
        return answer

# [1, 1, 4, 2, 1, 1, 0, 0]
nums = [73, 74, 75, 71, 69, 72, 76, 73]
print(Solution().dailyTemperatures(nums))