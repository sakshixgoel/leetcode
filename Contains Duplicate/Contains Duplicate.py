class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans = False
        for i in range(len(nums)):
            if nums[i] in nums[i+1:]:
                ans = True
        return ans
        
