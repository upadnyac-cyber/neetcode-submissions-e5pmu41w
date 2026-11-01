class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []
        unique = set()

        for i in range(len(nums)):
            complement = -1 * nums[i]
            
            l = i+1
            r = len(nums)-1

            while l < r:
                total = nums[l] + nums[r]

                if total > complement:
                    r-=1
                elif total < complement:
                    l+=1
                else:
                    if (nums[i],nums[l],nums[r]) not in unique:
                        unique.add((nums[i],nums[l],nums[r]))
                        res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    
        return res