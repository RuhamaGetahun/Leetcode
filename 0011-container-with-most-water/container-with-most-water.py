class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l, r = 0, len(height) - 1

        # Calculation 
        while r > l:
            h = min(height[r], height[l])
            w = r - l 
            Area = h * w

            max_area = max(max_area, Area)

            if height[r] > height[l]:
                l += 1
            else:
                r -= 1

        return max_area 



