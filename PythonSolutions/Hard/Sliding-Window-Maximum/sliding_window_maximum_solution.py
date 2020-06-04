class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque

        max_arr = []
        window = deque()

        for i in range(len(nums)):
            if window and window[0] <= i - k:
                window.popleft()
            while window and nums[window[-1]] <= nums[i]:
                window.pop()
            window.append(i)
            if i >= k - 1:
                max_arr.append(nums[window[0]])
        return max_arr