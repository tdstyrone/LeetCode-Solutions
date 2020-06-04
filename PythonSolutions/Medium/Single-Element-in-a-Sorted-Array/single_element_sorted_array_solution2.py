class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        # ALTERNATIVE SOLUTION
        new_dict = {}
        for num in nums:
            if num not in new_dict:
                new_dict.update({num: 1})
            else:
                new_dict[num] += 1
