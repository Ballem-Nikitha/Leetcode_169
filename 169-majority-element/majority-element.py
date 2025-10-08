class Solution(object):
    def majorityElement(self, nums):
        mapper = {}
        n = len(nums)
        
        for num in nums:
            if num not in mapper:
                mapper[num] = 1
            else:
                mapper[num] += 1
        
        for key, val in mapper.items():
            if val > n // 2:
                return key
