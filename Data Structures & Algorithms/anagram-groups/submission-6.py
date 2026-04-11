class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hmap = defaultdict(list)

        for s in strs:
            count = [0]*26
            for i in s:
                count[ord(i)-ord('a')]+=1
            hmap[tuple(count)].append(s)
        return list(hmap.values())

        
            






        