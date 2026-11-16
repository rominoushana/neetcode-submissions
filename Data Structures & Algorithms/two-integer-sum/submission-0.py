class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        pair = {}

        for i, n in enumerate(nums):
            secondNum = target - n
            if secondNum in pair:
                return [pair[secondNum], i] 
            pair[n] = i
