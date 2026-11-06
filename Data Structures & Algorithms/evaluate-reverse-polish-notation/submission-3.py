class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for token in tokens:

            if token == "+":
                nums2 = stack.pop()
                nums1 = stack.pop()
                stack.append(nums1 + nums2)
            elif token == "-":
                nums2 = stack.pop()
                nums1 = stack.pop()
                stack.append(nums1 - nums2)
            elif token == "*":
                nums2 = stack.pop()
                nums1 = stack.pop()
                stack.append(nums1 * nums2)
            elif token == "/":
                nums2 = stack.pop()
                nums1 = stack.pop()
                stack.append(int(nums1 / nums2))
            else:
                stack.append(int(token))
        
        return stack[0]
        