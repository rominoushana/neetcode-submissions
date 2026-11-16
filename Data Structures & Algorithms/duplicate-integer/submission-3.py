class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        currentNum = None
        nonDup = set()
        for i in nums:
            if i in nonDup:
                return True
            nonDup.add(i)
        return False