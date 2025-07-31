class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def time_taken(rate):
            time = 0
            # Calculate total time needed at this harvest rate
            for i in range(len(piles)):
                # Ceiling division: (apples[i] + rate - 1) // rate
                time += (piles[i] + rate - 1) // rate 
            return time <= h 

        # Binary search bounds: minimum rate = 1, maximum rate = max apples
        left, right = 1, max(piles)
        
        # Binary search for minimum valid harvest rate
        while left < right:
            mid = (left + right) // 2
            if time_taken(mid):
                right = mid 
            else:
                left = mid + 1 
        return right # or left goth works 
       