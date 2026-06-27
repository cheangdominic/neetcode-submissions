class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        nums_set = set(nums)

        for n in nums_set:
            next_num = n + 1
            curr_streak = 1
            while next_num in nums_set:
                curr_streak += 1
                next_num += 1
            longest_streak = max(longest_streak, curr_streak)
        return longest_streak
            