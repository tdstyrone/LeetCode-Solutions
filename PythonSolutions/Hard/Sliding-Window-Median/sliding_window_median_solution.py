class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        from collections import deque

        med_arr = []
        window = deque(maxlen=k)

        for i in range(len(nums)):
            window.append(nums[i])
            if len(window) == k and k % 2 == 0:
                sort_vsn = sorted(window)
                median = (sort_vsn[int(k / 2)] + sort_vsn[int(k / 2) - 1]) / 2
                med_arr.append(median)
            elif len(window) == k:
                sort_vsn = sorted(window)
                median = (sort_vsn[int(k // 2)])
                med_arr.append(median)
        return med_arr