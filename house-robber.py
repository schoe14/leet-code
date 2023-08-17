class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            temp = n + rob2
            rob2 = rob1
            rob1 = temp
        return max(rob1, rob2)