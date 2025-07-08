from collections import Counter

class FindSumPairs:

    def __init__(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2
        self.cnt = Counter(nums2)

    def add(self, index, val):
        _nums2, _cnt = self.nums2, self.cnt

        _cnt[_nums2[index]] -= 1
        _nums2[index] += val
        _cnt[_nums2[index]] += 1

    def count(self, tot):
        _nums1, _cnt = self.nums1, self.cnt
        ans = 0
        for num in _nums1:
            rest = tot - num
            ans += _cnt.get(rest, 0)
        return ans
