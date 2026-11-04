class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        m = max(piles)
        n = 1
        res = m

        while n <= m:

            mid = (m+n)//2
            total_time = 0

            for pile in piles:
                total_time+= math.ceil(pile/mid)

            if total_time <= h:
                res = min(res,mid)
                m = mid - 1
            else:
                n = mid + 1
                
            
        return res
                
        