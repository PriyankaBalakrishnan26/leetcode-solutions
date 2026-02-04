class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans= [0] * len(nums)
        total=0
        for i in range (len(nums)):
            total+= nums[i]
            ans[i]=total
        return ans
        