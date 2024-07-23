from collections import Counter

class Solution:
    def mostFrequent(self, nums, key) -> int:
        c = Counter()
        for i, n in enumerate(nums):
            if n == key and i + 1 < len(nums):
                c[nums[i + 1]] += 1
        return c.most_common(1)[0][0]