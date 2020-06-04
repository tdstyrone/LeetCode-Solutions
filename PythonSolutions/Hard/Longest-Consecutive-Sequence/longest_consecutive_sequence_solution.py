class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numbers = set(nums)
        longest_seq = 0

        for i in range(len(nums)):
            current_seq = 1
            if (nums[i] - 1) not in numbers:
                while (nums[i] + 1) in numbers:
                    current_seq += 1
                    nums[i] += 1
                longest_seq = max(longest_seq, current_seq)
        return longest_seq