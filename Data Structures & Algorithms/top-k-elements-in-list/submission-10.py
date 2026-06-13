class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        res = [[] for i in range(len(nums) + 1)]
        res_list = []
        counter = 0;

        for n in nums:
            hash_map[n] = hash_map.get(n, 0) + 1
        
        for n in hash_map:
            res[hash_map[n]].append(n)
        
        for n in range(len(res) - 1,  -1, -1):
            for num in res[n]:
                res_list.append(num)
                counter += 1
                if len(res_list) == k:
                    return res_list
        return []