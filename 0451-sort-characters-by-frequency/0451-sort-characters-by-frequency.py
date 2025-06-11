from collections import Counter

class Solution(object):
    def frequencySort(self, s):
        freq = Counter(s)  # Count frequencies of each character
        sorted_chars = sorted(freq.keys(), key=lambda x: (-freq[x], x))  # Sort by frequency (descending)
        result = ''.join(char * freq[char] for char in sorted_chars)  # Build result string
        return result
