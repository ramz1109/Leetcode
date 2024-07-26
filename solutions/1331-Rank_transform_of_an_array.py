from collections import defaultdict

class Solution:
    def arrayRankTransform(self, arr):
        sorted_arr = sorted(arr)
        my_dict = defaultdict(int)

        cnt = 1
        for num in sorted_arr:
            if num not in my_dict:
                my_dict[num] = cnt
                cnt += 1
        
        res = []
        for num in arr:
            res.append(my_dict[num])
        
        return res