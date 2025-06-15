class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            n = sum(int(i) ** 2 for i in str(n))
            if n in seen:
                return False
            seen.add(n) # why did it make difference when I changed where it was sitting 
            
        return True 
 
        