class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #hash-maps 
        l, r = 0, len(nums) - 1
        res = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in res:
                return [res[complement], i]
            res[num] = i  # store num we have already seen.. 
