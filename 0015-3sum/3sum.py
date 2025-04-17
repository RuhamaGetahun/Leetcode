class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        store = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            l, r = i + 1, len(nums) - 1 

            while l < r :
                evaluation = nums[i] + nums[l] + nums[r]
                if evaluation == 0:
                    store.append([nums[i], nums[l], nums[r]])
                    l , r = l + 1 , r - 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1

                elif evaluation < 0:
                    l += 1 
                else:
                    r -=1 
        return store 

    