class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {"(": ")", "{": "}", "[": "]"}
        bracket_start = ["(", "{", "["]
        lastBracket = -1

        for i in range(len(s)):
            if s[i] in bracket_start:
                stack.append(s[i])
            elif len(stack) == 0:
                return False
            elif (bracket_map[(stack[lastBracket])] == s[i]):
                stack.pop()
            else:
                return False

        if len(stack) == 0:
            return True
        return False