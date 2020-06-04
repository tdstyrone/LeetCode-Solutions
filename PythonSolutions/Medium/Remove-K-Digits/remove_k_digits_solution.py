class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        stack = []
        num_remove = k
        for n in num:
            while num_remove and stack and stack[-1] > n:
                stack.pop()
                num_remove -= 1
            stack.append(n)
        result = "".join(stack[:len(num) - k]).lstrip("0")

        if len(result):
            return result
        else:
            return "0"