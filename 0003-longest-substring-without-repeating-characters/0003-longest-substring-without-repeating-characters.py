class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        max_len = 0
        char_index_map = {}

        for right in range(len(s)):
            if s[right] in char_index_map:
                left = max(left, char_index_map[s[right]] + 1)
            max_len = max(max_len, right - left + 1)
            char_index_map[s[right]] = right
        
        return max_len

        
        