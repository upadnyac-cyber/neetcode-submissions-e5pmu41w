class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        track = {}
        l = 0
        max_freq = max_len = 0

        for r in range(len(s)):

            track[s[r]] = 1 + track.get(s[r],0)
            max_freq = max(max_freq, track[s[r]])

            if ((r-l+1) - max_freq) > k:
                track[s[l]]-=1
                l+=1
            
            max_len = max(max_len,r-l+1)
        
        return max_len
                