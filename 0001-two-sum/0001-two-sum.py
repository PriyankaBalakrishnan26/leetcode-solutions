class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, j in enumerate(nums):
            check_val = target - j
            if check_val == j:
                try:
                    second_index = nums.index(check_val,i+1)
                    return [i, second_index ]
                except:
                    continue
            elif check_val in nums:
                return [i, nums.index(check_val) ]
