class Solution:
    def longestPalindrome(self, s: str) -> str:

        a = [0,0]

        def scan(i,j):
            u = i
            v = j

            while u >= 0 and v < len(s) and s[u] == s[v]:
                u-=1
                v+=1

            return v-u-1


        for i in range(len(s)):
            oddLen = scan(i,i)
            if oddLen > (a[1]-a[0])+1:
                dist = oddLen//2
                a = [i-dist,i+dist]
            
            evenLen = scan(i,i+1)
            if evenLen > (a[1]-a[0])+1:
                dist = evenLen//2
                a = [i-dist+1,i+dist]
        
        i,j = a

        return s[i:j+1]

        

        