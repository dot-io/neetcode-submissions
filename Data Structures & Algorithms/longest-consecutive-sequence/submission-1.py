class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        i = 0
        max_seq_len = 0
        while i < len(nums):
            seq_number = 1
            if not nums[i] - 1 in num_set:
                while nums[i] + seq_number in num_set:
                    print(nums[i] + seq_number)
                    seq_number += 1
            i += 1
            if seq_number > max_seq_len:
                max_seq_len = seq_number

        return max_seq_len         
