class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        def backtrack(curr, curSum, i):
            if curSum == target:
                res.append(curr.copy())
                return
            if curSum > target:
                return
            if i < len(nums):
                curSum+=nums[i]
                curr.append(nums[i])
                backtrack(curr,curSum,i)
                curSum-=nums[i]
                curr.pop()
                backtrack(curr,curSum,i+1)
        
        backtrack([],0,0)

        return res
        