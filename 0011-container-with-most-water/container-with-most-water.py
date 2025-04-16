class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_Area = 0 
        l , r = 0, len(height) - 1

        while l < r:
            h = min(height[l], height[r])
            w = r - l 
            Area = h * w 

            max_Area = max(max_Area, Area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_Area 



