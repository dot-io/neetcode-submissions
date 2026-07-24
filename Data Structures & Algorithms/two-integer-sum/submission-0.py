class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for j, m in enumerate(nums):
            target_diff = target - m
            for i, n in enumerate(nums[:j]):
                if n == target_diff:
                    return [i, j]