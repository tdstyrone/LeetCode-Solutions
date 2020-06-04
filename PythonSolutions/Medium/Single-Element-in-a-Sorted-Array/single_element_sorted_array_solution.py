class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        from collections import Counter
        new_dict = Counter(nums)

        for key, value in new_dict.items():
            if value == 1:
                return key
