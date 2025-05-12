class Solution(object):
    def strStr(self, haystack, needle):
        if haystack=="":
            return 0
        return haystack.find(needle)
        