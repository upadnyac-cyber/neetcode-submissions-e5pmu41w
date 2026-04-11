class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hmap = {}

        for i in range(len(nums)):
            hmap[nums[i]]=i

        for i in range(len(nums)):

            y = target - nums[i]
            if y in hmap and i != hmap[y]:
                return [i, hmap[y]]


        
        