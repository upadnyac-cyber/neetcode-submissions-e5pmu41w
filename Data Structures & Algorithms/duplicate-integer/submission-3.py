class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hmap = {}
        value = 0

        for i in nums:

            if i in hmap:
                return True
            hmap[i]=i
        
        return False

        