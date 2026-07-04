class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #int nums. return true, if value twice (duplicates allowed - ) in nums[i], return false if i distinct
        if len(nums) == len(set(nums)):
            return False
        return True
