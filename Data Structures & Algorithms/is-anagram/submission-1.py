class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        smap,tmap = {},{}

        for i in s:
            smap[i]=1+smap.get(i,0)
        for i in t:
            tmap[i]=1+tmap.get(i,0)

        if smap == tmap:
            return True
        return False


        