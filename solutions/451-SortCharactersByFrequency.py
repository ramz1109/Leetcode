from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        counted = Counter(s)
        sorted_counted = dict(sorted(counted.items(), key=lambda x:x[1], reverse=True))
        res = ""

        for key, value in sorted_counted.items():
            for _ in range(value):
                res += key
        
        return res