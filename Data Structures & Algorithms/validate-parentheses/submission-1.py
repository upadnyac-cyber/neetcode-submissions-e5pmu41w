class Solution:
    def isValid(self, s: str) -> bool:

        mapping = {"]":"[","}":"{",")":"("}
        stack = []

        for bracket in s:
            if bracket in mapping:
                last = stack.pop() if stack else "#"
                if mapping[bracket] != last:
                    return False
            else:
                stack.append(bracket)
        
        if not stack:
            return True
        else:
            return False

        