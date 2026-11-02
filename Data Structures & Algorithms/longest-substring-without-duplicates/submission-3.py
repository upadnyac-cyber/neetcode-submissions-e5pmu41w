class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        unique = set()
        l = maxLen = 0

        for r in range(len(s)):
            if s[r] in unique:
                while s[r] in unique:
                    unique.discard(s[l])
                    l+=1

            unique.add(s[r])
            maxLen = max(maxLen,r-l+1)
        
        return maxLen

        