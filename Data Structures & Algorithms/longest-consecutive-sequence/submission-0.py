class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        unique = set()
        count = 0
        maxcount = 0

        for i in range(len(nums)):
            unique.add(nums[i])
        
        for num in nums:
            if num-1 in unique:
                continue
            
            while num in unique:
                count+=1
                num+=1
            maxcount = max(maxcount,count)
            count = 0
        
        return maxcount


            

        
        return maxcount
        