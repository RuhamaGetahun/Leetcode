class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        start = 0 
        sum_nums = {}
        current_sum = 0 
        max_sum = 0 

        for end in range(len(nums)):
            sum_nums[nums[end]] = sum_nums.get(nums[end], 0) + 1
            current_sum += nums[end]

            while end - start + 1  > k:
                sum_nums[nums[start]] -= 1 
                current_sum -= nums[start]
                if sum_nums[nums[start]] == 0:
                    del sum_nums[nums[start]]
                start += 1 

            if end - start + 1 and len(sum_nums) == k:
                max_sum = max(max_sum, current_sum)

        return max_sum 
