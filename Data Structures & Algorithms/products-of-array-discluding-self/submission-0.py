class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        length = len(nums)
        leftprod = 1
        rightprod = [0] * length
        res = [0] * length
        rightprod[length-1] = nums[length-1]

        for i in range(length-2,0,-1):
            rightprod[i]= rightprod[i+1] * nums[i]
        
        for i in range(length-1):
            res[i] = leftprod * rightprod[i+1]
            leftprod *=nums[i]
        
        res[length-1] = leftprod

        return res
        
        