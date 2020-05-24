class Solution:
    def twoSum(self, nums, target):
        idx_dict = {}
        diff = 0

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in idx_dict:
                idx_dict.update({nums[i]: i})
            else:
                return [idx_dict[diff], i]