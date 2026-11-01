class Solution:
    def maxArea(self, heights: List[int]) -> int:

        r = len(heights)-1
        l = 0
        water = 0
        max_water = 0

        while l < r:

            water = min(heights[l],heights[r]) * (r-l)
            max_water = max(water,max_water)

            if heights[l] < heights[r]:
                l+=1
            elif heights[l] > heights[r]:
                r-=1
            else:
                if l < r and heights[l+1] > heights[r-1]:
                    l+=1
                else:
                    r-=1
        
        return max_water
        