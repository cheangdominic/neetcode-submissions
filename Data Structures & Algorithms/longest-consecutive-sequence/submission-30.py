class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        nums_set = set(nums)

        for n in nums_set:
            next_num, curr_streak = n + 1, 1
            while next_num in nums_set:
                curr_streak += 1
                next_num += 1
            longest_streak = max(curr_streak, longest_streak)
        return longest_streak