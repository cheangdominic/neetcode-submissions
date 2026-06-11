class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i, n in enumerate(nums):
            product = 1
            for j, t in enumerate(nums):
                if j != i:
                    product *= t
            res.append(product)

        return res