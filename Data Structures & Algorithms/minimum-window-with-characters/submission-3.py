class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not t or t == "":
            return ""

        countT = {}

        for i in t:
            countT[i] = 1 + countT.get(i,0)
        
        need = len(countT)
        have = 0

        window = {}
        l = 0
        resLen = float("inf")
        res = [-1,-1]

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)

            if c in countT and countT[c] == window[c]:
                have+=1
            
            while need == have:
                if (r-l+1) < resLen:
                    resLen = r-l+1
                    res = [l,r]
                window[s[l]]-=1
                if s[l] in countT and countT[s[l]] > window[s[l]]:
                    have -=1
                
                l+=1

        l,r = res

        return s[l:r+1] if resLen != float("inf") else ""

            
