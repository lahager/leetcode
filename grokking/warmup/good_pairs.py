class Solution:
    def numIdenticalPairs(self, nums):
        pairCount = 0
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
            if counts[n] > 1:
                pairCount += counts[n] - 1
        return pairCount

        