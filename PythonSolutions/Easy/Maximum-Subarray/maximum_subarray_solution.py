class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_total_point = 0
        max_total = 0

        for elem in nums:
            max_total_point += elem
            if max_total_point < 0:
                max_total_point = 0
            elif max_total_point > max_total:
                max_total = max_total_point

        if max_total == 0:
            return max(nums)
        return max_total