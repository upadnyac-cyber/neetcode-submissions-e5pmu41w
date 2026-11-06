class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        res = [0] * len(temperatures)

        for idx,temp in enumerate(temperatures):

            while stack and temp > stack[-1][1]:
                s_idx,s_temp = stack.pop()
                res[s_idx] = (idx - s_idx)
            
            stack.append([idx,temp])
        
        return res
            


        