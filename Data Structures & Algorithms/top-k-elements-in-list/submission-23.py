class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        frequency_list = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            frequency_map[n] = frequency_map.get(n, 0) + 1

        for n, c in frequency_map.items():
            frequency_list[c].append(n)
        
        res = []
        for i in range(len(frequency_list) - 1, -1, -1):
            for s in frequency_list[i]:
                res.append(s)
                if len(res) >= k:
                    return res