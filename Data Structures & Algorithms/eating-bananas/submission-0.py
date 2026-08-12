class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        tmin, tmax = 1,max(piles)
        res = tmax

        while(tmin<=tmax):
            mid = tmin + (tmax - tmin) // 2
            hrs = 0
            for x in piles:
                hrs += (x+mid-1)//mid

            if hrs <= h:
                res = min(res, mid)
                tmax = mid-1
            else: tmin = mid + 1
        return res
