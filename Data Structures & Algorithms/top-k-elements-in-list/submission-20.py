class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_list = [[] for _ in range(len(nums) + 1)]
        frequency_map = {}

        for n in nums:
            frequency_map[n] = frequency_map.get(n, 0) + 1
        
        for n, c in frequency_map.items():
            frequency_list[c].append(n)
        
        res = []
        for n in range(len(frequency_list) - 1, -1, -1):
            for c in frequency_list[n]:
                res.append(c)
                if len(res) >= k:
                    return res