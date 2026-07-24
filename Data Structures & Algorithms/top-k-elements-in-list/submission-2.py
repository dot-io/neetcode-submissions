class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        for n in nums:
            if n not in frequency_map.keys():
                frequency_map[n] = 0
            frequency_map[n] += 1
        return sorted(frequency_map.keys(),key=lambda x: frequency_map[x], reverse=True)[:k]
