class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1 
        seen = {} # hash 

        for i , num in enumerate(nums): # iterate 
            complement = target - num 

            if complement in seen:
                return ([seen[complement], i])

            seen[num] = i 
            