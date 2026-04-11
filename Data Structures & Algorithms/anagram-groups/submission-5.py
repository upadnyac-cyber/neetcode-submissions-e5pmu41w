class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hmap = defaultdict(list)

        for i in strs:
            sorted_i = ''.join(sorted(i))
            hmap[sorted_i].append(i)
        return list(hmap.values())

        
            






        