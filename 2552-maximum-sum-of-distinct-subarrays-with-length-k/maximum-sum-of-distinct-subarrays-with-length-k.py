class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        start = 0 
        sum_nums = set()
        current_sum = 0 
        max_sum = 0 

        for end in range(len(nums)):
            while nums[end] in sum_nums:
                sum_nums.remove(nums[start])
                current_sum -= nums[start]
                start += 1 
            
            sum_nums.add(nums[end])
            current_sum += nums[end]

            if len(sum_nums) == k:
                max_sum = max(max_sum, current_sum)
                sum_nums.remove(nums[start])
                current_sum -= nums[start]
                start += 1 

        return max_sum 
