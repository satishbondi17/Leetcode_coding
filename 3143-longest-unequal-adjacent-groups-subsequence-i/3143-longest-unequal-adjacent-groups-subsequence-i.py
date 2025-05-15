class Solution(object):
    def getLongestSubsequence(self, words, groups):
        
        result = [words[0]]
        prev_group = groups[0]

        for i in range(1, len(words)):
            if groups[i] != prev_group:
                result.append(words[i])
                prev_group = groups[i]
        
        return result
       