class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        hmap = {}

        for i in nums:
            hmap[i] = 1 + hmap.get(i,0)

        sorted_i = dict(sorted(hmap.items(), key=lambda item: item[1], reverse=True))

        ans = list(sorted_i)[:k]

        return ans
            
        

        

        