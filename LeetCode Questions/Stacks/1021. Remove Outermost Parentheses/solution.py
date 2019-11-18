class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = ""
        count = 0
        inner_stack = ""
        for i in range(len(S)):
            inner_stack += S[i]
            if S[i] == '(':
                count += 1
                continue
            elif S[i] == ')':
                count -= 1
            if count == 0:
                stack += inner_stack[1:-1]
                inner_stack = ""
        return stack

print(Solution().removeOuterParentheses("(()())(())(()(()))"))