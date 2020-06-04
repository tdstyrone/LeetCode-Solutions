class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_set = set(nums)

        for numbers in num_set:
            if nums.count(numbers) > (len(nums) / 2):
                return numbers