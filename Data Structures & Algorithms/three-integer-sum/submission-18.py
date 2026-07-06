class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort_list = sorted(nums)
        tuple_list = []
        for c in range(len(sort_list) - 2):
            if c > 0 and sort_list[c] == sort_list[c-1]:
                continue
            l = c + 1
            r = len(sort_list) - 1
            while l < r:
                sum_val = sort_list[c] + sort_list[l] + sort_list[r]
                if sum_val > 0:
                    r -= 1
                elif sum_val < 0:
                    l += 1
                else:
                    tuple_list.append([sort_list[c], sort_list[l], sort_list[r]])
                    while l < r and sort_list[l] == sort_list[l+1]:
                        l += 1
                    while l < r and sort_list[r] == sort_list[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return tuple_list