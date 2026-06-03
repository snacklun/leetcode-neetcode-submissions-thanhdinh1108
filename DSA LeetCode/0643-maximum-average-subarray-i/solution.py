class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = 0
        for x in range(0,k):
            total += nums[x]
        temp_total = total
        for r in range(k,len(nums)):
            temp_total += nums[r] - nums[r-k]
            total = max(total, temp_total)
        return total / k
