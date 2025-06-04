class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        Valid_triangles = 0 

        for i in range(len(nums) - 1, 1 , -1):
            l = 0 
            r = i -1 

            while l < r :
                if nums[l] + nums[r] > nums[i]:
                    Valid_triangles += r - l 
                    r -= 1

                else:
                    l += 1 
        
        return Valid_triangles 

            