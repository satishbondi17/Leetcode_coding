from collections import Counter

class Solution(object):
    def robotWithString(self, s):
        freq = Counter(s)
        stack = []
        res = []
        min_char = 'a'

        for c in s:
            stack.append(c)
            freq[c] -= 1

            while min_char <= 'z' and freq[min_char] == 0:
                min_char = chr(ord(min_char) + 1)

            while stack and stack[-1] <= min_char:
                res.append(stack.pop())

        return ''.join(res)
