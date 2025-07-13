class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(subset, i):
            if i == len(nums):
                res.append(subset[:])
                return 

            subset.append(nums[i])
            backtrack(subset, i + 1)

            subset.pop()
            backtrack(subset, i + 1)

        res = []
        backtrack([], 0)
        return res
        