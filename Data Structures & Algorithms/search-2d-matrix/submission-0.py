class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rlen,clen = len(matrix)-1, len(matrix[0])-1

        top = 0
        bot = rlen

        while top <= bot:
            midr = (top+bot)//2

            if target > matrix[midr][-1]:
                top = midr +1
            elif target < matrix[midr][0]:
                bot = midr - 1
            else:
                break

        if not top <= bot:
            return False
        
        l = 0
        r = l+clen

        while l<=r:
            m = (l+r)//2

            if target == matrix[midr][m]:
                return True
            
            if target > matrix[midr][m]:
                l = m + 1
            else:
                r = m -1
        
        return False

