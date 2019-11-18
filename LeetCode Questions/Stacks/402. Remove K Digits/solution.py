class Solution(object):
    def removeKdigits(self, num, k):
        # if the number of digits to be removed is the same as the length, remove all the digits and return zero
        if len(num) == k:
            return '0'
        # create our stack
        stack = []
        # iterate through the digits in the num variable
        for n in num:
            # while there is a stack and the number is less than the last element on the stack and K is greater than zero
            while stack and n < stack[-1] and k:
                # remove the last element
                stack.pop()
                # decrease k
                k -= 1
            # if the number is not a leading zero
            if stack or n != '0':
                # add that number to the stack
                stack.append(n)
        # if there are still elements in num to be removed, pop the stack and decrease K
        while stack and k:
            stack.pop()
            k-= 1
        # if the stack is empty return zero
        if not stack:
            return '0'
        # return the stack as a string
        return(''.join(stack))


print(Solution().removeKdigits(num = "10", k = 1))
print(Solution().removeKdigits(num = "10200", k = 1))
# print(Solution().removeKdigits(num = "1432219", k = 3))