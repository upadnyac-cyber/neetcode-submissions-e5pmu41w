class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        def backtrack(curr,i):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for idx in range(len(nums)):
                if nums[idx] in curr:
                    continue
                curr.append(nums[idx])
                backtrack(curr,idx+1)
                curr.pop()
            
        backtrack([],0)
        return res