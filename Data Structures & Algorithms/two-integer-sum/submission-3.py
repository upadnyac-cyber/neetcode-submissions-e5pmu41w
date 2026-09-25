class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for i in range(0,len(nums)):
            hmap[nums[i]] = i

        for i in range(0,len(nums)):
            x = target - nums[i]
            if x in hmap:
                j = hmap[x]
                if i!=j:
                    return [i,j]