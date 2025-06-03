class Solution(object):
    def isValid(self, s):
        stack = []
        for i in s:
            if i in "([{":
                stack.append(i)
            else:
                if not stack:
                    return False
                ch = stack.pop()
                if not ((i == ')' and ch == '(') or 
                        (i == ']' and ch == '[') or 
                        (i == '}' and ch == '{')):
                    return False
        return len(stack) == 0


       