class Solution:
    def sortArray(self, nums):
        def counting_sort():
            counts = {}

            min_val, max_val = min(nums), max(nums)

            for num in nums:
                counts[num] = counts.get(num, 0) + 1

            index = 0
            for num in range(min_val, max_val+1, 1):
                while counts.get(num, 0) > 0:
                    nums[index] = num
                    index += 1
                    counts[num] -= 1
        
        counting_sort()
        return nums