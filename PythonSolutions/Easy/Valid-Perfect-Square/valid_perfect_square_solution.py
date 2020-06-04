class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        sqrt = num ** 0.5
        if (sqrt % 1 == 0):
            return True
        else:
            return False