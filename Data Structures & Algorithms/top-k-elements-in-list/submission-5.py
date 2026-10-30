class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = {}
        res = []

        for n in nums:
            counter[n]= 1 + counter.get(n,0)
        
        freq = defaultdict(list)
        for val in counter:
            freq[counter[val]].append(val)
        
        for i in range(len(nums),0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        

        