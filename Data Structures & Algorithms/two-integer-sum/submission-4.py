class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        index_map = {}
        find = 0

        for i in range(len(nums)):
            index_map[nums[i]] = i
        
        for i in range(len(nums)):
            find = target - nums[i]
            if find in index_map:
                if i != index_map[find]:
                    return [i,index_map[find]]

        

        