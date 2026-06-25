class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_arr = [[] for _ in range(len(nums) + 1)]
        count_map = {}

        for n in nums:
            count_map[n] = count_map.get(n, 0) + 1

        for n, c in count_map.items():
            count_arr[c].append(n)
        
        res = []
        for n in range(len(count_arr) - 1, -1, -1):
            for s in count_arr[n]:
                res.append(s)
                if len(res) >= k:
                    return res
            