class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #if nums have duplicates, return True
        #if nums distinct [no duplicates - use set], return False
        if len(nums) == len(set(nums)):
            return False
        return True
