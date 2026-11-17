class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        pair = {}

        for index, val in enumerate(nums):
            diff = target - val
            if diff in pair:
                return [pair[diff], index]
            pair[val] = index