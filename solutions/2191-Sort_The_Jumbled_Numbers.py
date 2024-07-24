class Solution:
    def sortJumbled(self, mapping, nums):
        my_store = []

        for k in range(len(nums)):
            temp = ''
            for i in str(nums[k]):
                temp += str(mapping[int(i)])
            my_store.append((int(temp), k))
        
        my_store.sort()
        res = []
        for pair in my_store:
            res.append(nums[pair[1]])
        return res