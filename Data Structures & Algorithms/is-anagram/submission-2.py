class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        counter = [0]*26

        for c in s:
            counter[ord(c) - ord('a')] +=1
        
        for c in t:
            counter[ord(c)-ord('a')] -=1

        for count in counter:
            if count:
                return False

        return True      